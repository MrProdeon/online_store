# mypy: ignore-errors

import pytest

from src.category_iterator import CategoryIterator


def test_category_iterator(category_init):
    result = CategoryIterator(category_init)
    assert next(result) == "Банан, 100 руб. Остаток: 4 шт."
    assert next(result) == "Яблоко, 50 руб. Остаток: 2 шт."
    with pytest.raises(StopIteration):
        assert next(result)
