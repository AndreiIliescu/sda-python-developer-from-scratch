### Abstract classes ###
from abc import ABC, abstractmethod
from math import pi

class Figure(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Implementarea functiei permimeter
    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    # Functia __eq__ este folosita automat de python atunci cand compara doua obiecte
    # (atunci cand folosim operatorul ==)
    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * self.r * pi

    def area(self):
        return pi * self.r ** 2

rect = Rectangle(10, 5)
print(f'rect permieter is {rect.perimeter()}')

circle = Circle(8)
print(f'circle area is: {circle.area()}')

my_rect1 = Rectangle(5, 5)
my_rect2 = Rectangle(5, 5)
print(my_rect1 == circle)
