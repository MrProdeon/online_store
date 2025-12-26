class QuantityException(Exception):

    def __init__(self, message : str) -> None:
        self.message = message if message else "Товар с нулевым количеством не может быть добавлен"

    def __str__(self) -> str:
        return self.message
