# mypy: ignore-errors
from unittest.mock import patch

import src.product


def test_product_init(product_init):
    assert product_init.name == "Банан"
    assert product_init.description == "Жёлтый"
    assert product_init.price == 100
    assert product_init.quantity == 4


def test_product_price_setter_zero_or_less(product_init, capsys):
    product_init.price = -1
    msg = capsys.readouterr()

    assert msg.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_price_setter(product_init):
    product_init.price = 1000

    assert product_init.price == 1000


@patch("builtins.input")
def test_product_price_setter_approve_yes(mock_input, product_init):
    product = product_init
    mock_input.return_value = "y"
    product.price = 80

    assert product.price == 80


@patch("builtins.input")
def test_product_price_setter_approve_no(mock_input, product_init):
    product = product_init
    mock_input.return_value = "n"
    product.price = 80

    assert product.price == 100


def test_new_product(product_init):
    product = product_init.new_product({"name": "Персик", "description": "вкусный", "price": 50, "quantity": 2}, [])

    assert isinstance(product, src.product.Product)


def test_alrready_have_product(product_init):

    product = product_init.new_product(
        {"name": "Банан", "description": "тест", "price": 150, "quantity": 2}, [product_init]
    )
    assert product.price == 150
    assert product.quantity == 6
    assert product.name == "Банан"
    assert product.description == "тест"
