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


def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number(10) == 10
    assert Item.string_to_number('1256') == 1256


def test__repr__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__str__():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test__add__():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Наушники", 20000, 15)
    assert item1 + item2 == 35

