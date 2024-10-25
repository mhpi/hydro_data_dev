import icechunk
import numpy as np
import xarray as xr

from pathlib import Path

from core.Config import Config

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

    store = icechunk.IcechunkStore.open_existing(
        storage=storage_config,
        mode="r",
    )
    ds = xr.open_zarr(store, zarr_format=3, consolidated=False)
    return ds

def create_config(file: Path | str) -> Config:
    if isinstance(file, str):
        file = Path(file)

    if not file.exists():
        raise FileNotFoundError(f"YAML file not found: {file}")

    return Config.from_yaml(file)

def calculate_statistics(ds: xr.Dataset, config: Config) -> dict[str, np.ndarray]:
    """A function to calculate statistics from a dataset

    Parameters
    ----------
    ds : xr.Dataset
        The dataset to calculate statistics from

    Returns
    -------
    xr.Dataset
        The dataset with statistics calculated
    """
    variables = [config.static_variables, config.time_series_variables, config.target_variables]
    data = 
    statDict = {}
    for k in range(len(seriesLst)):
        var = seriesLst[k]
        sub_data = data[..., k]
        sub_data_flat = sub_data.flatten()
        sub_data_remove_nan = sub_data_flat[~np.isnan(sub_data_flat)]
        mean = np.mean(sub_data_remove_nan).astype(float)
        std = np.std(sub_data_remove_nan).astype(float)
        std = np.maximum(std, 0.001)
        statDict[var] = [None, None, mean, std]
    return statDict
