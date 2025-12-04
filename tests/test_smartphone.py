# mypy: ignore-errors

import pytest

from src.smartphone import Smartphone


@pytest.fixture
def get_smartphone():
    return Smartphone("iphone", "cool", 100_000, 1, 1, "17", 256, "white")


def test_smartphone_init(get_smartphone):
    assert get_smartphone.name == "iphone"
    assert get_smartphone.description == "cool"
    assert get_smartphone.price == 100000
    assert get_smartphone.quantity == 1
    assert get_smartphone.efficiency == 1
    assert get_smartphone.model == "17"
    assert get_smartphone.memory == 256
    assert get_smartphone.color == "white"
