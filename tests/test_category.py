# mypy: ignore-errors

import src.product


def test_category_init(category_init):
    assert category_init.name == "Фрукты"
    assert category_init.description == "Свежие"
    assert len(category_init.products) == 2

    for product in category_init.products:
        assert isinstance(product, src.product.Product)


def test_category_counter(category_init):
    assert category_init.count_of_categories == 1


def test_product_count(category_init):
    assert category_init.count_of_products == 2
