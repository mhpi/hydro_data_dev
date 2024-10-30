from pathlib import Path

import icechunk
import numpy as np
import xarray as xr

from hydro_data_dev.core.Config import Config

__all__ = ["fetch_data"]


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
