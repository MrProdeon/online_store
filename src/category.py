class Category:
    """
    Класс для создания объектов категорий продуктов. В списке продуктов должен хранить экземпляры
    класса Product
    """

    name: str
    description: str
    products: list

    count_of_categories = 0
    count_of_products = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.count_of_categories += 1
        Category.count_of_products += len(self.products)
