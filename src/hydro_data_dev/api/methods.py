from pathlib import Path

import icechunk
import numpy as np
import xarray as xr
import yaml

from hydro_data_dev.core.methods import _calc_stats
from hydro_data_dev.core.Record import Record

__all__ = [
    "create_record",
    "fetch_data",
    "generate_scaler",
]


def fetch_data(record: Record) -> xr.Dataset:
    """A function to fetch data from an s3 bucket using icechunk, then subsetting for the data you want

    Note: Jiangtao Liu's load_nc() function is used partially in this function

    Parameters
    ----------
    record : Record
        A Record object representing the configuration parameters

    Returns
    -------
    xr.Dataset
        The sliced dataset fetched from the s3 bucket
    """
    storage_config = icechunk.StorageConfig.s3_anonymous(
        bucket=record.bucket,
        prefix=record.dataset,
        region=None,
        endpoint_url=None,
    )

    try:
        store = icechunk.IcechunkStore.open_existing(
            storage=storage_config,
            mode="r",
        )
    except ValueError as e:
        raise ValueError(f"Error opening the dataset: {record.dataset} from {record.bucket}") from e
    ds = xr.open_zarr(store, zarr_format=3, consolidated=False)

    station_ids = record.station_ids.read_text().splitlines()
    if station_ids is not None:
        ds = ds.sel(station_ids=[int(station_ids) for station_ids in station_ids])

    selected_vars = []
    if record.time_series_variables:
        selected_vars.extend(record.time_series_variables)
    if record.static_variables:
        selected_vars.extend(record.static_variables)
    if record.target_variables:
        selected_vars.extend(record.target_variables)
    if selected_vars:
        ds = ds[selected_vars]
    return ds


def create_record(
    record: str | Path,
) -> Record:
    """A function to create a Record object from a yaml file

    Parameters
    ----------
    record : str | Path
        A string or Path object representing the path to the yaml file

    Returns
    -------
    Record
        A Record object representing the configuration parameters
    """
    if isinstance(record, str):
        record = Path(record)
    record_dict = yaml.safe_load(record.read_text())
    record_obj = Record(**record_dict)
    return record_obj


def generate_scaler(
    forcing_data: xr.Dataset | None,
    static_data: xr.Dataset,
    observational_data: xr.Dataset,
) -> dict[str, np.ndarray]:
    """A function to generate a scaler dictionary for the data

    Parameters
    ----------
    forcing_data : xr.Dataset
        The forcing data
    static_data : xr.Dataset
        The static data
    """
    scaler = {}
    if forcing_data is not None:
        scaler["x_mean"], scaler["x_std"] = _calc_stats(forcing_data.values, axis=(0, 1))
    scaler["y_mean"], scaler["y_std"] = _calc_stats(observational_data.values, axis=(0, 1))
    scaler["c_mean"], scaler["c_std"] = _calc_stats(static_data.values)
    return scaler
