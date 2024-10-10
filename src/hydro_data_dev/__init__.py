from importlib.metadata import version

from hydro_data_dev._registry.api import build
from hydro_data_dev.Record import Record

__version__ = version("hydro_data_dev")
del version
