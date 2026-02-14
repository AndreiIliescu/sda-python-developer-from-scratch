from typing import Self


class Animal:
    pass
    # def __init__(self):
    #     print(Self)


a = Animal()
b = Animal()

print(type(a))
print(type(a) == Animal)
print(isinstance(a, Animal))
