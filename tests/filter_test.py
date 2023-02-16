import pytest
from main import filter_
import datafile


@pytest.mark.parametrize("data, expected", [(datafile.geo_logs, datafile.geo_logs_exp),
                                            (datafile.geo_logs2, datafile.geo_logs2_exp),
                                            (datafile.geo_logs3, datafile.geo_logs3_exp)])
def test_filter(data, expected):
    res = filter_(data)
    assert res == expected
