import pytest
from src.phone import Phone


@pytest.fixture
def phone_for_test():
    return Phone('Карандаши', 30, 100, 3)

def test_number_of_sim(phone_for_test):
    assert phone_for_test.number_of_sim == 3

