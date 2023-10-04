import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard_for_test():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_change_lang(keyboard_for_test):
    assert keyboard_for_test.language == 'EN'

    keyboard_for_test.change_lang()
    assert keyboard_for_test.language == 'RU'

    keyboard_for_test.change_lang()
    assert keyboard_for_test.language == 'EN'


def test_error(keyboard_for_test):
    """Ошибка выскочит если ящык не RU или EN"""
    with pytest.raises(AttributeError):
        keyboard_for_test.language = 'CH'


def test_language(keyboard_for_test):
    """Можно поменять язык просто приравняв нужный атрибут, но при условии, что это будет RU или EN"""
    keyboard_for_test.language = 'RU'
    assert keyboard_for_test.language == 'RU'
