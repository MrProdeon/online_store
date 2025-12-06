from src.product import Product
from abc import ABC, abstractmethod

class OrderCategory(ABC):

    @abstractmethod
    def __init__(self, description):
        self.description = description

    @abstractmethod
    def __str__(self):
        pass


class Category(OrderCategory):
    """
    Класс для создания объектов категорий продуктов. В списке продуктов должен хранить экземпляры
    класса Product
    """

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        super().__init__(description)
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """Строковое представление, которое указывает на название категории
        и количество товаров в этой категории"""
        total_quantity = 0
        for product in self.products_in_list:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Метод для записи объекта класса Product или его дочерних классов в список товаров (в атрибут __products)"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только экземпляры класса Product или его дочерних классов")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Метод для получения продуктов"""
        products_string = ""
        for product in self.__products:
            products_string += f"{str(product)}\n"
        return products_string

    @property
    def products_in_list(self) -> list:
        """Геттер для получения списка продуктов"""
        return self.__products
