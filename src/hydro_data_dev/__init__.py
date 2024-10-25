from hydro_data_dev._version import version as __version__
from hydro_data_dev.api.methods import fetch_data

# in case setuptools scm screw up and find version to be 0.0.0
assert not __version__.startswith("0.0.0")

__all__ = [
    "fetch_data",
    "calculate_statistics",
]
