import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_init():
    return Product("Банан", "Жёлтый", 100, 4)


@pytest.fixture
def category_init():
    Category.count_of_categories = 0
    Category.count_of_products = 0
    return Category("Фрукты", "Свежие", [Product("Банан", "Жёлтый", 100, 4), Product("Яблоко", "Зелёное", 50, 2)])
