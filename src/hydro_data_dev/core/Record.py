from datetime import datetime
from pathlib import Path
from typing import Any

from pydantic import BaseModel, field_validator, model_validator

DATE_FORMAT = "%Y-%m-%d"


def _check_path(v: str) -> Path:
    """A function to determine if a path exists or not

    Parameters
    ----------
    v : str
        A string representing a path

    Returns
    -------
    Path
        A Path object representing the path
    """
    path = Path(v)
    if not path.exists():
        cwd = Path.cwd()
        raise ValueError(f"Path {v} does not exist. CWD: {cwd}")
    return path


class Record(BaseModel):
    """A dataclass to represent config inputs for your data fetching"""

    bucket: str
    dataset: str
    train_date_range: tuple[str, str]
    val_date_range: tuple[str, str]
    test_date_range: tuple[str, str]
    time_series_variables: list[str]
    target_variables: list[str]
    static_variables: list[str]
    station_ids: str

    @model_validator(mode="after")
    @classmethod
    def validate_dates(cls, config: Any) -> Any:
        """A function to format str dates into datetime objects

        Parameters
        ----------
        config : Any
            A dictionary of configuration parameters

        Returns
        -------
        Any
            A dictionary of configuration parameters with datetime objects
        """
        try:
            config.train_date_range = tuple(
                datetime.strptime(date_string, DATE_FORMAT) for date_string in config.train_date_range
            )
        except ValueError as e:
            raise ValueError("Error converting train_date_range to datetime") from e
        try:
            config.val_date_range = tuple(
                datetime.strptime(date_string, DATE_FORMAT) for date_string in config.val_date_range
            )
        except ValueError as e:
            raise ValueError("Error converting val_date_range to datetime") from e
        try:
            config.test_date_range = tuple(
                datetime.strptime(date_string, DATE_FORMAT) for date_string in config.test_date_range
            )
        except ValueError as e:
            raise ValueError("Error converting test_date_range to datetime") from e
        return config

    @field_validator(
        "station_ids",
    )
    @classmethod
    def validate_data_dir(cls, v: str) -> Path:
        """A function to validate the data directory

        Parameters
        ----------
        v : str
            A string representing a path

        Returns
        -------
        Path
            A Path object representing the path

        """
        return _check_path(v)
