import pytest
from src.phone import Phone


@pytest.fixture
def phone_for_test():
    return Phone('Карандаши', 30, 100, 3)


def test_number_of_sim(phone_for_test):
    """Проверяет правильно ли выводится колличество симок"""
    assert phone_for_test.number_of_sim == 3


def test_number_of_sim_value_zero():
    """Симок не должно быть 0"""
    phone_for_test.number_of_sim = 0
    assert pytest.raises(ValueError)
