import pytest
from src.phone import Phone


@pytest.fixture
def item2():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_number_of_sim(item2):
    assert item2.number_of_sim == 2
    item2.number_of_sim = 3
    assert item2.number_of_sim == 3


def test_repr(item2):
    assert repr(item2) == "Phone('iPhone 14', 120000, 5, 2)"