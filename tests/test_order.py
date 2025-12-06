# mypy: ignore-errors
from src.order import Order
from src.product import Product

product = Product("Банан", "Жёлтый", 100, 4)
order = Order("Как можно быстрее", product, 2)


def test_order_init():
    assert order.description == "Как можно быстрее"
    assert str(order.product) == "Банан, 100 руб. Остаток: 4 шт."
    assert order.price == 100
    assert order.quantity == 2
    assert order.total_price == 200
    assert str(order) == "Состав заказа : Банан, в количестве 2шт; общая стоимость 200"
