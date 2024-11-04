from pathlib import Path

import pytest

import hydro_data_dev as hdd


@pytest.fixture
def sample_record() -> hdd.Record:
    path = Path(__file__).parent / "data" / "example_record.yaml"
    return hdd.create_record(record=path)
