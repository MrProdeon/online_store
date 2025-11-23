# mypy: ignore-errors
import pytest

import src.product


def test_category_init(category_init):
    assert category_init.name == "Фрукты"
    assert category_init.description == "Свежие"
    assert len(category_init.products_in_list) == 2

    for product in category_init.products_in_list:
        assert isinstance(product, src.product.Product)


def test_category_counter(category_init):
    assert category_init.count_of_categories == 1


def test_product_count(category_init):
    assert category_init.count_of_products == 2


def test_get_product(category_init):
    assert category_init.products == "Банан, 100 руб. Остаток: 4 шт.\nЯблоко, 50 руб. Остаток: 2 шт.\n"


def test_get_products_in_list(category_init):
    assert len(category_init.products_in_list) == 2
    for product in category_init.products_in_list:
        assert isinstance(product, src.product.Product)


def test_add_product_error(category_init, capsys):
    with pytest.raises(ValueError, match="Можно добавлять только экземпляры класса Product"):
        category_init.add_product("123")


def test_add_product(category_init, product_init):
    assert category_init.count_of_products == 2

    category_init.add_product(product_init)

    assert category_init.count_of_products == 3
