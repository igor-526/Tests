from main import unical_ids
import datafile
import pytest


@pytest.mark.parametrize("data, expected", [(datafile.ids, datafile.ids_exp),
                                            (datafile.ids2, datafile.ids2_exp)])
def test_ids(data, expected):
    res = unical_ids(data)
    assert res == expected
