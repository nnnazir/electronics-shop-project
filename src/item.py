import os.path
import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = 'Файл item.csv поврежден'

    def __str__(self):
        return self.message


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
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Не дочерний класс Item')
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов.')

    @classmethod
    def instantiate_from_csv(cls, file=os.path.join(os.path.dirname(__file__), 'items.csv')):
        """
        класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """
        cls.all = []
        try:
            with open(file, 'r', newline='', encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for i in reader:
                    if list(i) == ['name', 'price', 'quantity']:
                        name, price, quantity = i['name'], float(i['price']), int(i['quantity'])
                        cls(name, price, quantity)
                    else:
                        raise InstantiateCSVError('Файл item.csv поврежден')
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(num):
        """
        статический метод, возвращающий число из числа-строки
        """
        number = int(float(num))
        return number