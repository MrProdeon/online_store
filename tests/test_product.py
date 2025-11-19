# mypy: ignore-errors

def test_product_init(product_init):
    assert product_init.name == "Банан"
    assert product_init.description == "Жёлтый"
    assert product_init.price == 100
    assert product_init.quantity == 4
