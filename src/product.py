class Product:
    """
    Класс для создания объектов продукта, для последующей передачи в класс Category
    """
    name: str
    description: str
    price: int | float
    quantity: int

    def __init__(self, name : str, description : str, price : int | float, quantity : int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
