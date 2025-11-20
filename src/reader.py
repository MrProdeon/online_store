import json

from src.category import Category
from src.product import Product

path = "products.json"


def json_reader(path : str) -> list[dict]:
    """Чтение json-файла и преобразование его в пайтон-объект.
    В случае неудачи вернет список с пустым словарем"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else: return [{}]
    except Exception:
        return [{}]


def create_object_from_json(data : list[dict]) -> list:
    """
    Функция для прохождения по списку словарей и формирования экземпляров класса Category
    и Product
    :param data: список словарей с данными для преобразования
    :return: Список, в котором каждый элемент - это экземпляр класса Category,
    а атрибут list в нём - экземпляр класса Product
    """
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
