class Product:
    """
    Класс для создания объектов продукта, для последующей передачи в класс Category
    """

    name: str
    description: str
    price: int | float
    quantity: int

    def __init__(self, name: str, description: str, price: int | float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_params : dict, products_list : list):
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
                    product.__price = product_params["price"]

                product.description = product_params.get("description", product.description)

                return product

        return cls(**product_params)

    @property
    def price(self):
        """Метод для получения цены продукта"""
        return self.__price

    @price.setter
    def price(self, new_price : int | float):
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





