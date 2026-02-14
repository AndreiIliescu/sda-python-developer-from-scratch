import datetime
import uuid

from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price, qtt, desc):
        self.name = name
        self.price = price
        self.quantity = qtt
        self.description = desc
        self.unique_code = str(uuid.uuid4())

    @abstractmethod
    def total_value(self) -> int:
        pass

    def __str__(self):
        return f'{self.name} x {self.quantity}'

    def __repr__(self):
        return f'{self.name} x {self.quantity}'


class FoodProduct(Product):
    def __init__(self, name, price, qtt, desc, expiration):
        super().__init__(name, price, qtt, desc)
        self.expiration_date = expiration

    def is_expired(self) -> bool:
        return self.expiration_date <= datetime.date.today()

    def total_value(self) -> int:
        if not self.is_expired():
            return self.price * self.quantity

        return 0

class ElectronicProduct(Product):
    def __init__(self, name, price, qtt, desc):
        super().__init__(name, price, qtt, desc)

    def total_value(self) -> int:
        return self.price * self.quantity
