from datetime import datetime
from pathlib import Path

import icechunk
import numpy as np
import xarray as xr

from hydro_data_dev.core.methods import _calc_stats
from hydro_data_dev.core.Record import Record

__all__ = [
    "create_record",
    "fetch_data",
    "generate_scaler",
]


def fetch_data(bucket: str, dataset: str) -> xr.Dataset:
    """A function to fetch data from an s3 bucket using icechunk

    Parameters
    ----------
    bucket : str
        The name of the s3 bucket
    dataset : str
        The name of the dataset

    Returns
    -------
    xr.Dataset
        The dataset fetched from the s3 bucket
    """
    storage_config = icechunk.StorageConfig.s3_anonymous(
        bucket=bucket,
        prefix=dataset,
        region=None,
        endpoint_url=None,
    )

    try:
        store = icechunk.IcechunkStore.open_existing(
            storage=storage_config,
            mode="r",
        )
    except ValueError as e:
        raise ValueError(f"Error opening the dataset: {dataset} from {bucket}") from e
    ds = xr.open_zarr(store, zarr_format=3, consolidated=False)
    return ds


def create_record(
    basin_ids: list[str] | Path | None,
    time_range: tuple[str, str] | None,
    attribute_names: list[str] | None,
    forcing_names: list[str] | None,
) -> Record:
    if basin_ids is not None:
        if isinstance(basin_ids, Path):
            basin_ids: list[str] = basin_ids.read_text().splitlines()
    if time_range is not None:
        date_strings = time_range
        if len(date_strings) != 2:
            raise ValueError("time_range must contain exactly two date strings")
        time_range: tuple[datetime, datetime] = tuple(datetime.strptime(date, "%Y-%m-%d") for date in date_strings)
    record = Record(
        basin_ids=basin_ids,
        time_range=time_range,
        attribute_names=attribute_names,
        forcing_names=forcing_names,
    )
    return record


def generate_scaler(
    forcing_data: xr.Dataset,
    static_data: xr.Dataset,
    observational_data: xr.Dataset,
) -> dict[str, np.ndarray]:
    scaler = {}
    scaler["x_mean"], scaler["x_std"] = _calc_stats(forcing_data.values, axis=(0, 1))
    scaler["y_mean"], scaler["y_std"] = _calc_stats(observational_data.values, axis=(0, 1))
    scaler["c_mean"], scaler["c_std"] = _calc_stats(static_data.values)
    return scaler
