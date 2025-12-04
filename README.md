

## Онлайн-магазин

### В репозитории происходит разработка бэкенда для онлайн магазина

## Установка и использование:
1) Клонируйте репозиторий к себе на компьютер с помощью команды `git clone`
2) Проект использует poetry, поэтому для использования проекта установите его. И установите зависимости с помощью `poetry install`
3) Точка входа на данный момент не используется, но добавлена для будущего - main.py

# Функционал проекта:

## Пакет src :

- Модуль category:  
Представлен класс Category
С обязательными атрибутами при инициализации:
```python
name: str # название продукта
description: str # описание продукта
products : list # Продукты (в основном экземпляры класса Product)
```
Присутствуют атрибуты класса для подсчета категорий и для подсчета продуктов:
```python
count_of_categories = 0 #подсчет созданных экземляров категорий 
product_count = 0 #подсчет продуктов в категориях
```

Пример использования:
```
fruits = Category("Фрукты", "Свежие", [Product("Банан", "Жёлтый", 100, 4), Product("Яблоко", "Зелёное", 50, 2)])

fruits.name >> Фрукты
fruits.descriptio >>
fruits.products (геттер) >> 
Банан, количество продуктов: 4шт.
Яблоко, количество продуктов: 2шт.

```

Методы класса:

str - Строковое представление, которое указывает на название категории
и количество товаров в этой категории 
Пример использования:
```python
str(fruits)
>>>
'''Банан, количество продуктов: 4шт.
Яблоко, количество продуктов: 2шт.'''
```

add_product(self, product: Product)
Метод для записи объекта класса Product или его дочерних классов в список товаров (в атрибут __products)
Пример использования:
```python

from category import Category
from product import Product

# Создаём категорию
smartphones = Category("Смартфоны")

# Создаём продукты
iphone = Product(name="iPhone 15", price=1200, quantity=5)
samsung = Product(name="Samsung S23", price=900, quantity=3)

# Добавляем товары в категорию
smartphones.add_product(iphone)
smartphones.add_product(samsung)

print(smartphones.products)
>>> """iPhone 15, количество продуктов: 5
Samsung S23,  количество продуктов: 3
"""

```

Геттер products  
Получение продуктов, где каждый продукт будет в формате f"{self.name}, количество продуктов: {total_quantity} шт.",  
при этом каждый продукт на новой строке  
Пример использования:
```python
fruits.products
>> 
'''Банан, количество продуктов: 4шт.
Яблоко, количество продуктов: 2шт.'''
```

Геттер products_in_list  
Получение списка с объектами продуктов по категории 
Пример использования:
```python
fruits.products_in_list
>> 
[объект класса Product, объект класса Product]
```




- Модуль product:  
Представлен класс Product  
Атрибутов класса нет.  
С обязательными атрибутами при инициализации:
```python
name: str # название продукта
description: str # описание продукта
__price: int | float # цена продукта
quantity: int # количество
```

Пример использования:
```python

banana = Product("Банан", "Жёлтый", 100, 4)
banana.name >> Банан
banana.description >> Жёлтый
banna.price >> 100 (price вынесен в геттер, так как он защищен)
banana.quantity >> 4
```


Доступные методы :

str - вернет строку в формате f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."  
Пример использования:
```python
str(banana)
>>> 'Банан, 100 руб. Остаток : 4 шт.'
```  

add - получение суммы при сложении продуктов. Сложение идет по всему количеству на складе.  
Пример использования:
```python
result = banana + apple
>>> 200
```

new_product(cls, product_params: dict, products_list: list["Product"]) -> "Product"  
Класс-метод для создания нового объекта продукта.  
Если объект с таким именем уже есть, преобразует старый объект, вместо создания нового.  
Если цена нового больше, то ставит ту, что больше.  
Количество складывается.  
Если описание новое передано, то будет новое. Если нет, то старое.  
```python
from product import Product

# Список существующих продуктов
products = [
    Product(name="iPhone 15", price=1000, quantity=5, description="Флагман Apple"),
    Product(name="Samsung S23", price=900, quantity=3, description="Флагман Samsung"),
]

# Новые данные о продукте
new_item_data = {
    "name": "iPhone 15",
    "price": 1200,           # новая цена выше — старая обновится
    "quantity": 2,           # количество прибавится (5 + 2)
    "description": "Обновлённая версия описания"
}

# Создаём или обновляем продукт
updated_product = Product.new_product(new_item_data, products)

print(updated_product.name)        # iPhone 15
print(updated_product.price)       # 1200 (старая была 1000 → обновилась)
print(updated_product.quantity)    # 7   (5 + 2)
print(updated_product.description) # "Обновлённая версия описания"

# Новый список продуктов
print(products)

```

Геттер price - получение защищенного атрибута цены товара
Пример использования:
```python
banana.price
>>> 100
```

Сеттер price - изменение цены продукта.  В случае отрицательной цены - ничего не изменит.  
Пример использования:
```python
banana.price = 200
print(banana.price)
>>> 200
```

### Модуль smartphone
Описан класс Smartphone, наследник класса Product.
```python
# Создаём объект смартфона
iphone = Smartphone(
    name="iPhone 15",
    description="Флагманский смартфон Apple",
    price=1200.0,
    quantity=5,
    efficiency=95.5,
    model="A3090",
    memory=256,
    color="Black"
)


print(iphone.name)         # iPhone 15
print(iphone.model)        # A3090
print(iphone.memory)       # 256

# Можно использовать методы родительского класса Product
print(iphone.get_total_price())  # 1200 * 5 = 6000


```

### Модуль lawngrass

Описан класс LawnGrass, наследник класса Product.
Пример использования:
```python
# Создаём объект газонной травы
grass = LawnGrass(
    name="GreenField Universal",
    description="Универсальная газонная трава для дачи",
    price=899.0,
    quantity=10,
    country="Germany",
    germination_period="7–14 дней",
    color="Зелёный"
)


print(grass.name)                # GreenField Universal
print(grass.country)             # Germany
print(grass.germination_period)  # 7–14 дней

print(grass.get_total_price())   # 899 * 10 = 8990

```


- Модуль readers, в котором расположены функции :
1) для прочтения JSON-файла и преобразования его в объект пайтон.  
json_reader(path) - принимает путь до JSON-файла и возвращает пайтон-объект или список с пустым словарём,
если не удалось открыть.

Пример использования:
```python
result = json_reader(path)

print(result)

[
  {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ]
  },
  {
    "name": "Телевизоры",
    "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    "products": [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ]
  }
]
```
2) Для создания экземпляров класса Category и Product из списка словарей, полученного путём чтения JSON-файла  
Принимает на вход список словарей и возвращает список, в который добавлены экземпляры класса Category, при этом 
список продуктов представлен ввиде экземпляров класса Product.  

Пример использования:
```python
result = create_object_from_json(data)

print(result)

# [<src.category.Category object at 0x00000226DA26A1E0>, <src.category.Category object at 0x00000226DA26A480>]


```

  



## Тесты
Для всех модулей проекта были написаны тесты с помощью pytest  

## Документация и ссылки  
На данный момент проект не использует стороннюю документацию  


## Лицензия
На данный момент у проекта нет лицензии