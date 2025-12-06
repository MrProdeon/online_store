# mypy: ignore-errors

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_init():
    return Product("Банан", "Жёлтый", 100, 4)


@pytest.fixture
def product_init2():
    return Product("Киви", "Зелёный", 100, 4)


@pytest.fixture
def category_init():
    Category.category_count = 0
    Category.product_count = 0
    return Category("Фрукты", "Свежие", [Product("Банан", "Жёлтый", 100, 4), Product("Яблоко", "Зелёное", 50, 2)])


@pytest.fixture
def json_load_mock():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации,"
            " но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]
