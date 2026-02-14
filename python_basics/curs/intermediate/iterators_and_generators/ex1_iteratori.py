# Implementati iteratorul CountDown
class CountDown:
    def __init__(self, start):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 0:
            raise StopIteration

        # Current este numarul la care am ajuns
        current = self.num
        self.num -= 1
        return current

c = CountDown(4)
print(next(c))
print(next(c))
print(next(c))
print(next(c))

# output:
# 4
# 3
# 2
# 1
for elem in CountDown(4):
    print(elem)
