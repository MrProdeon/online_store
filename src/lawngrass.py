from src.product import Product


class LawnGrass(Product):
    """Класс для создания объектов газонаю.
    Данный класс наследуется от класса Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: int | float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
