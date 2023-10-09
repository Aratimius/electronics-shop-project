from src.item import Item


class Phone(Item):
    """Класс для телефонов"""
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    # Переписываю __repr__ под класс Phone
    def __repr__(self):
        return super().__repr__().rstrip(')') + f', {self._number_of_sim})'

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value == 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
