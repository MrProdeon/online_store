from src.category import Category


class CategoryIterator:
    """Класс для итерации по продуктам в экземпляре класса Category.
    Принимает экземпляр класса Category и проходит по его атрибуту products_in_list,
    перебирая все элементы один за другим"""

    def __init__(self, category: Category):
        self.index = 0
        self.category = category

    def __iter__(self) -> "CategoryIterator":
        return self

    def __next__(self) -> str:
        if self.index < len(self.category.products_in_list):
            product = str(self.category.products_in_list[self.index])
            self.index += 1
            return product
        else:
            raise StopIteration
