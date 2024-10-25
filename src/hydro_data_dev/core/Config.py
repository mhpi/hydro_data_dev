import yaml
from pydantic import BaseModel, computed_field
from pathlib import Path

class Config(BaseModel):
    """
    Configuration model running deep learning simulations.

    Attributes
    ----------
    bucket : str
        The name of the bucket.
    dataset : str
        The name of the dataset.
    train_date_list : List[str]
        List of training dates.
    val_date_list : List[str]
        List of validation dates.
    test_date_list : List[str]
        List of test dates.
    time_series_variables : List[str]
        List of time series variables.
    target_variables : List[str]
        List of target variables.
    static_variables : List[str]
        List of static variables.
    station_ids : Path
        Path to the file containing station IDs.
    add_coords : bool
        Flag to add coordinates.
    group_mask_dict : Optional[Dict]
        Dictionary for group masks.
    data_type : str
        Type of the data.
    """

    bucket: str
    dataset: str
    train_date_list: list[str]
    val_date_list: list[str]
    test_date_list: list[str]
    time_series_variables: list[str]
    target_variables: list[str]
    static_variables: list[str]
    station_ids: Path
    add_coords: bool
    group_mask_dict: dict | None
    data_type: str

    @computed_field
    @property
    def station_list(self) -> list[str]:
        """Read station IDs from file"""
        return self.station_ids.read_text().splitlines()

    @classmethod
    def from_yaml(cls, path: Path) -> "Config":
        """
        Create a Config instance from a YAML file.

        Parameters
        ----------
        path : str | Path
            The path to the YAML file.

        Returns
        -------
        Config
            An instance of the Config class.
        """
        data = yaml.safe_load(path.read_text())
        return cls(**data)
