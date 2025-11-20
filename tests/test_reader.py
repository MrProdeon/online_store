from unittest.mock import mock_open, patch
import json

import src.category
from src.reader import json_reader, create_object_from_json


def test_json_reader(json_load_mock):
    json_data = json_load_mock

    with patch("builtins.open", mock_open()) as mock_file:
        with patch("json.load") as mock_json_load:
            mock_json_load.return_value = json_data

            result = json_reader("products.json")

            mock_file.assert_called_once_with("products.json", "r", encoding="utf-8")
            mock_json_load.assert_called_once()

            assert result == json_data

def test_json_reader_error():
    result = json_reader(123)

    assert result == [{}]


def test_create_object_from_json(json_load_mock):
    result = create_object_from_json(json_load_mock)
    assert len(result) == 1
    assert isinstance(*result,src.category.Category)

    category = result[0]
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"

    product = category.products[0]
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.price == 180000.0