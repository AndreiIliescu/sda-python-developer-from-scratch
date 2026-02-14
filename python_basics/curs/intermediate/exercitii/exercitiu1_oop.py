class Animals:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def who_am_i(self):
        print(f'I am {self.name}, I weigh {self.weight}kg, and I am {self.age} years old.')

    def look(self):
        print('I am looking')

    def breath(self):
        print('I am breathing')


class Fish(Animals):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)

    def swim(self):
        print('I am swimming')

class Mammal(Animals):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)

    def run(self):
        print('I am running')

class Bird(Animals):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)

    def fly(self):
        print('I am flying')

class DomesticDog(Mammal):
    def __init__(self, name, weight, age, breed, coat_color):
        super().__init__(name, weight, age)

        self.breed = breed
        self.coat_color = coat_color

    def bark(self):
        print('Woof woof!')

    def retrieve(self):
        print('I am retrieving')

dog1 = DomesticDog('Waffle', 10, 10, 'Jackrussel', 'brown')
dog1.who_am_i()
dog1.run()
