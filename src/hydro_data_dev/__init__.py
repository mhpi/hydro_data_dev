from hydro_data_dev._version import version as __version__
from hydro_data_dev.api.methods import create_record, fetch_data, generate_scaler
from hydro_data_dev.core.Record import Record

# in case setuptools scm screw up and find version to be 0.0.0
assert not __version__.startswith("0.0.0")

__all__ = [
    "fetch_data",
    "create_record",
    "generate_scaler",
]
