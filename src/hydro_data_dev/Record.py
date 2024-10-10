import logging
from enum import Enum
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, field_validator, model_validator
from pydantic.dataclasses import dataclass

class BMINameEnum(str, Enum):
    land_surface_air__temperature = "land_surface_air__temperature"

class BMIUnitEnum(str, Enum):
    degC = "degC"

class FormatEnum(str, Enum):
    zarr = "zarr"

@dataclass
class Forcing:
    name: BMINameEnum
    units: BMIUnitEnum
    
@dataclass
class Attribute:
    name: BMINameEnum
    units: BMIUnitEnum
    
@dataclass
class Metadata:
    name: str
    root: Path
    version: str

class Record(BaseModel):
    meta: Metadata
    start_time: datetime
    end_time: datetime
    format: FormatEnum
    attributes: Optional[List[Attribute]]  
    forcings: Optional[List[Forcing]]
    
