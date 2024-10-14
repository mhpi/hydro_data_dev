from pathlib import Path
from typing import Any

import xarray as xr
import pytest

current_dir = Path.cwd()

@pytest.fixture
def sample_json() -> dict[str, Any]:
    record = {
        "meta": {
            "name": "sample_camels",
            "root": (current_dir / "sample_data/sample_camels.nc").__str__(),
            "version": "v1.0.0"
        },
        "data": xr.open_dataset(current_dir / "sample_data/sample_camels.nc", engine="netcdf4"),
        "start_time": '1980-01-01T00:00:00.000000000',
        "end_time": '2014-12-31T00:00:00.000000000',
        "format": "netcdf",
    }
    return record
