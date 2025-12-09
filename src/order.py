import src.product
from src.category import OrderCategory


class Order(OrderCategory):
    """Класс заказа, может содержать только один заказанный товар.
    Наследуется от абстрактного класса OrderCategory, который так же является родителем класса Category,
    берет из него описание и обязательный метод __str__

    Имеет метод для рассчитывания общей стоимости заказа, исходя из цены и кол-ва

    Для строкового представления вернет информация о составе заказа, кол-во товаров и общей стоимости
    """

    def __init__(self, description: str, product: src.product.Product, quantity: int) -> None:
        super().__init__(description)
        self.product = product
        self.price = product.price
        self.quantity = quantity

    @property
    def total_price(self) -> int | float:
        return self.price * self.quantity

    def __str__(self) -> str:
        return (
            f"Состав заказа : {self.product.name}, в количестве {self.quantity}шт; общая стоимость {self.total_price}"
        )
