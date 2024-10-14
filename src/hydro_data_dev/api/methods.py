import json
from pathlib import Path
from typing import Any

import xarray as xr
import zarr

from hydro_data_dev.core.record import Record

__all__ = ["record", "save_record", "load_record"]

def record(data: xr.Dataset) -> Record:
    """Creates a hydrologic data record

    Parameters
    ----------
    kwargs
        Passed through to the :func:`Record` constructor

    Returns
    -------
    Record
        The record object
    """
    return Record(**kwargs)

def record_from_dict(**kwargs: Any) -> Record:
    """Creates a hydrologic data record

    Parameters
    ----------
    kwargs
        Passed through to the :func:`Record` constructor

    Returns
    -------
    Record
        The record object
    """
    return Record(**kwargs)


def save_record(record: Record, path: Path) -> None:
    """Save a record to a file

    Parameters
    ----------
    record : Record
        The record to save
    path : Path
        The path to save the record to

    Raises
    ------
    OSError
        If an error occurs writing to the file
    TypeError
        If the data is not JSON serializable
    """
    data = record.model_dump_json(indent=2)
    try:
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except OSError as e:
        raise OSError(f"Error writing to file {path}: {e}") from e
    except TypeError as e:
        raise TypeError(f"Data is not JSON serializable: {e}") from e


def load_record(path: Path) -> Record:
    """Load a record from a json file

    Parameters
    ----------
    path : Path
        The path to the json file

    Returns
    -------
    Record
        The record object
    """
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return Record(**data)
