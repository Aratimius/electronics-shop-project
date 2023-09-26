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
    with pytest.raises(AttributeError):
        keyboard_for_test.language = 'CH'


def test_language(keyboard_for_test):
    keyboard_for_test.language = 'RU'
    assert keyboard_for_test.language == 'RU'
