from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, product_params: dict, products_list: list["Product"]) -> "Product":
        pass

    @property
    @abstractmethod
    def price(self) -> int | float:
        """Геттер метода price"""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price : int | float) -> None:
        """Сеттер метода price"""
        pass


class MixinRepr:
    """Миксин для вывода технической информации о созданном объекте"""

    def __init__(self) -> None:
        print(self.__repr__())

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})" # type: ignore


class Product(MixinRepr, BaseProduct):
    """
    Класс для создания объектов продукта, для последующей передачи в класс Category
    Наследуется от абстрактного класса BaseProduct
    Имеет миксин MixinRepr для вывода технической информации в консоль
    """

    name: str
    description: str
    __price: int | float
    quantity: int

    def __init__(self, name: str, description: str, price: int | float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """Строковое представление для продукта.
        Выведет имя, цену и количество."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> int | float:
        """Реализация сложения двух продуктов.
        Сложение идет по всем имеющимся продуктам.(Всё количество)"""
        if type(other) is type(self):
            first_product = self.price * self.quantity
            second_product = other.price * other.quantity
            return first_product + second_product
        raise TypeError

    @classmethod
    def new_product(cls, product_params: dict, products_list: list["Product"]) -> "Product":
        """
        Класс-метод для создания нового объекта продукта.
        Если объект с таким именем уже есть, преобразует старый объект, вместо создания нового.
        Если цена нового больше, то ставит ту, что больше.
        Количество складывается.
        Если описание новое передано, то будет новое. Если нет, то старое.
        """
        for product in products_list:
            if product_params["name"].lower() == product.name.lower():
                product.quantity += product_params["quantity"]

                if product_params["price"] > product.__price:
                    product.price = product_params["price"]

                product.description = product_params.get("description", product.description)

                return product

        return cls(**product_params)

    @property
    def price(self) -> int | float:
        """Метод для получения цены продукта"""
        return self.__price

    @price.setter
    def price(self, new_price: int | float) -> None:
        """Метод для изменения цены продукта. В случае отрицательной цены - ничего не изменит."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                approve = input("Введите Y для потдверждения снижения цены, N для отказа").lower()
                while approve not in ("y", "n"):
                    approve = input("Введите Y для потдверждения снижения цены, N для отказа").lower()
                if approve == "y":
                    self.__price = new_price
                else:
                    print("Цена не изменилась")
            else:
                self.__price = new_price
