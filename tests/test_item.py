import pytest
from src.item import Item

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000

def test_apply_discount():
    Item.pay_rate = 0.8
    item2 = Item("Ноутбук", 20000, 5)
    assert item2.price == 20000
    item1 = Item("Смартфон", 10000, 20)
    item1.apply_discount()
    assert item1.price == 8000
