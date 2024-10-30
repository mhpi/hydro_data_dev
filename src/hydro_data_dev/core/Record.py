from datetime import datetime
from pydantic.dataclasses import dataclass


@dataclass
class Record:
    """A dataclass to represent data inputs"""

    basin_ids: list[str] | None
    time_range: tuple[datetime, datetime] | None
    attribute_names: list[str] | None
    forcing_names: list[str] | None
