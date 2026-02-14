def make_sum_until(number):
    if number == 0:
        return 0
    else:
        return number + make_sum_until(number - 1)

def factorial_recursivity(number):
    if number == 1:
        return 1
    else:
        return number * factorial_recursivity(number - 1)


print(factorial_recursivity(5))
