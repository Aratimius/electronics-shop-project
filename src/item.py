import csv


class InstantiateCSVError(Exception):
    """Класс для кастомного исключения"""
    def __init__(self, *args, **kwargs):
        self.message = 'Файл .csv поврежден'


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
        # Вызов __init__ Миксинлога:
        super().__init__()

        self.__name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', " \
               f"{self.price}, {self.quantity})"

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return 'Одно из слагаемых не отвечает требованиям'

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
    def instantiate_from_csv(cls, filepath):
        """
        Классметод, считывающий информацию с csv-файла, и передающий данные в
        из файла для инициализации экземпляров класса Item
        """
        # Обработка исключения FileNotFoundError
        # quantity:
        #         1
        #         3
        #         5
        #         5
        #         5

        try:
            with open(filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                # Создание сразу нескольких экземпляров
                for row in reader:
                    try:
                        if len(row) < 3:
                            raise InstantiateCSVError
                    # Поймает нужную ошибку только тогда, когда удален один из столбцов
                    except InstantiateCSVError as ex:
                        raise InstantiateCSVError(ex.message)

                    cls.all.append(cls(row['name'], float(row['price']), int(row['quantity'])))
        except FileNotFoundError:
            raise FileNotFoundError('Файл не найден')

    @staticmethod
    def string_to_number(data_string) -> int:
        """Возвращает int из str"""
        return int(float(data_string))

    @property
    def name(self):
        """Возвращает наименование товара"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Если длинна наименования товара больше 10 -> обрежет до 10 символов"""
        if len(new_name) > 10:
            self.__name = new_name[:10].strip()
        else:
            self.__name = new_name
