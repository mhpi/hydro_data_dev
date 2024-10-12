from datetime import datetime
from enum import Enum
from pathlib import Path

from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class _bmi_name_enum(str, Enum):
    land_surface_air__temperature = "land_surface_air__temperature"


class _bmi_unit_enum(str, Enum):
    degC = "degC"


class _format_enum(str, Enum):
    zarr = "zarr"


class _mode_enum(str, Enum):
    a = "append"


@dataclass
class _forcing:
    name: _bmi_name_enum
    units: _bmi_unit_enum


@dataclass
class _attribute:
    name: _bmi_name_enum
    units: _bmi_unit_enum


@dataclass
class _metadata:
    name: str
    root: Path
    version: str


class Record(BaseModel):
    """A record containing information about a hydrological dataset"""

    meta: _metadata
    start_time: datetime
    end_time: datetime
    format: _format_enum
    mode: _mode_enum
    attributes: list[_attribute] | None
    forcings: list[_forcing] | None
