from pathlib import Path

import icechunk
import xarray as xr
import zarr
from dotenv import load_dotenv

# load_dotenv()

storage_config = icechunk.StorageConfig.s3_anonymous(
    bucket="mhpi-spatial",
    prefix="camels",
    region=None,
    endpoint_url=None,
)

store = icechunk.IcechunkStore.open_existing(
    storage=storage_config,
    mode="r",
)

# storage_config = icechunk.StorageConfig.s3_from_env(
#     bucket="mhpi-spatial",
#     prefix="camels",
# )
# try:
# store = icechunk.IcechunkStore.open_existing(
#     storage=storage_config,
#     mode="r",
# )
# # except ValueError:
# store = icechunk.IcechunkStore.create(storage_config)


# data_path = Path("/projects/mhpi/jql6620/format_data/26.pretrain_data_processing/01.insitu_and_basin_average/02.CAMELS/CAMELS_Dapeng.nc")
# ds = xr.open_dataset(data_path, engine="netcdf4")
# ds.to_zarr(store, zarr_format=3, consolidated=False)
# store.commit("adding CAMELS data")
ds = xr.open_zarr(store, consolidated=False)
print(ds)
