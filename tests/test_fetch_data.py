import hydro_data_dev as hdd


def test_fetch_data(sample_record: hdd.Record) -> None:
    ds = hdd.fetch_data(record=sample_record)

    assert ds.station_ids.values.shape[0] == 10
