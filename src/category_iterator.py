from src.category import Category
from src.product import Product


class CategoryIterator:

    def __init__(self, category : Category):
        self.category = category

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products_in_list):
            product = str(self.category.products_in_list[self.index])
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":
    test_category = Category("Фрукты", "Свежие",
                    [
                    Product("Банан", "Жёлтый", 100, 4),
                     Product("Яблоко", "Зелёное", 50, 2)
                    ]       )

    for i in CategoryIterator(test_category):
        print(i)