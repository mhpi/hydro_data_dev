from typing import Any

import pytest
from pydantic import ValidationError

import hydro_data_dev as hydro


def test_record(sample_json: dict[str, Any]):
    try:
        record = hydro.Record(**sample_json)
    except ValidationError as e:
        pytest.fail(e)

