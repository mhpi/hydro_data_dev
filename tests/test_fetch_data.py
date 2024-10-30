import pytest

import hydro_data_dev as hdd


def test_fetch_data() -> None:
    with pytest.raises(ValueError):
        hdd.fetch_data(bucket="test", dataset="test")
