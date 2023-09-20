from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    #Переписываю __repr__ под класс Phone
    def __repr__(self):
        return super().__repr__().rstrip(')') + f', {self.number_of_sim})'
