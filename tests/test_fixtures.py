import pytest


@pytest.mark.check
def test_change_name(user):
    # Check a changed name
    assert user.name == 'Oleksii'


@pytest.mark.check
def test_change_second_name(user):
    # Check a changed second name
    assert user.second_name == 'Stasiv'

