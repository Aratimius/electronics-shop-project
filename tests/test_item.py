"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_for_test():
    return Item('Карандаш', 30, 100)

def test_item_calculate_total_price(item_for_test):
    """Когда создаем экземпляр класса, то значение price и quantity то значение
    calculate_total_price будет:"""
    assert item_for_test.calculate_total_price() == 3000

def test_item_apply_discount(item_for_test):
    """ Применив apply_discount() значение price изменится на:"""
    item_for_test.pay_rate = 0.5
    item_for_test.apply_discount()
    assert item_for_test.price == 15

