from main import max_
import datafile
import pytest


@pytest.mark.parametrize('data, expected', [(datafile.stats, datafile.stats_exp),
                                            (datafile.stats2, datafile.stats2_exp),
                                            (datafile.stats3, datafile.stats3_exp),
                                            (datafile.stats4, datafile.stats4_exp)])
def test_max(data, expected):
    res = max_(data)
    assert res == expected
