import pytest
from dev2il_devops_app.main import get_root


def test_get_root_returns_dict():
    res = get_root()
    assert isinstance(res, dict)


@pytest.fixture
def it_works_dict():
    return {'it': "works!"}


def test_get_root_dict_contains_correct_pair(it_works_dict):
    res = get_root()
    assert res == it_works_dict
