import pytest
from dev2il_devops_app.main import get_fit


def test_get_fit_returns_dict():
    res = get_fit()
    assert isinstance(res, dict)


@pytest.fixture
def response_keys():
    return ['message', 'data_file', 'image_file']


def test_get_root_dict_contains_correct_keys(response_keys):
    res = get_fit()
    assert list(res.keys()) == response_keys
