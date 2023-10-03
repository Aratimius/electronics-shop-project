"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.item import InstantiateCSVError
from tests.test_phone import Phone


@pytest.fixture
def item_for_test():
    return Item('Карандаши', 30, 100)


def test_item_calculate_total_price(item_for_test):
    """Когда создаем экземпляр класса, то значение price и quantity то значение
    calculate_total_price будет:"""
    assert item_for_test.calculate_total_price() == 3000


def test_item_apply_discount(item_for_test):
    """ Применив apply_discount() значение price изменится на:"""
    item_for_test.pay_rate = 0.5
    item_for_test.apply_discount()
    assert item_for_test.price == 15


def test_name_len(item_for_test):
    """ Имя атрибута __name не должно содержать более 10 символов"""
    item_for_test.name = 'Карандаши цветные'
    assert item_for_test.name == 'Карандаши'


def test_string_to_numver():
    """string_to_number() должен переводить str в int"""
    assert Item.string_to_number('3') == 3


def test_instantiate_from_csv():
    """Проверка на чтение файла"""
    Item.instantiate_from_csv("../src/items.csv")
    assert Item.all[4].name == 'Клавиатура'


def test_str(item_for_test):
    assert str(item_for_test) == 'Карандаши'


def test_repr(item_for_test):
    assert repr(item_for_test) == 'Item(\'Карандаши\', 30, 100)'


def test_add():
    item1 = Item('Карандаши', 30, 100)
    phone1 = Phone('Карандаши', 30, 100, 3)

    assert item1 + phone1 == 200
    assert phone1 + phone1 == 200
    assert item1 + 100 == 'Одно из слагаемых не отвечает требованиям'


def test_file_corrupted():
    with pytest.raises(InstantiateCSVError, match='Файл .csv поврежден'):
        InstantiateCSVError('../src/corrupted.csv')
