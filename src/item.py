import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Классметод, считывающий информацию с csv-файла, и передающий данные в
        из файла для инициализации экземпляров класса Item
        """
        with open('../src/items.csv', newline='', encoding='Windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            # Создание сразу нескольких экземпляров
            for row in reader:
                cls.all.append(cls(row['name'], float(row['price']), int(row['quantity'])))

    @staticmethod
    def string_to_number(data_string) -> int:
        """Возвращает int из str"""
        return int(float(data_string))

    @property
    def name(self):
        """Возвращает наименование товара"""
        return self.__name

    @name.setter
    def name(self,new_name):
        """Если длинна наименования товара больше 10 -> обрежет до 10 символов"""
        if len(new_name) > 10:
            self.__name = new_name[:10].strip()
        else:
            self.__name = new_name
