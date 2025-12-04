# mypy: ignore-errors

import pytest

from src.lawngrass import LawnGrass


@pytest.fixture
def get_lawngrass():
    return LawnGrass("газон", "обычный", 100, 1, "Россия", "15", "зеленый")


def test_lawngrass_init(get_lawngrass):
    assert get_lawngrass.name == "газон"
    assert get_lawngrass.description == "обычный"
    assert get_lawngrass.price == 100
    assert get_lawngrass.quantity == 1
    assert get_lawngrass.country == "Россия"
    assert get_lawngrass.germination_period == "15"
    assert get_lawngrass.color == "зеленый"
