# from datetime import datetime

# def disable_at_night(func):
#     # a decorator that only calls a decorated function during the day
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()

#     return wrapper


# @disable_at_night
# def say_something():
#     print("Hello world")


# say_something()

# def outer(x): # 5
#     def inner(y): # 6
#         return x + y
#     return inner

# add_five = outer(5)
# result = add_five(6)
# print(result)  # prints 11


# def add(x, y):
#     return x + y

# def calculate(func, x, y):
#     return func(x, y)

# result = calculate(add, 4, 6)
# print(result)  # prints 10

# def greeting(name):
#     def hello():
#         return "Hello, " + name + "!"
#     return hello

# greet = greeting("Atlantis")
# print(greet())  # prints "Hello, Atlantis!"


# def make_pretty(func):
#     # define the inner function 
#     def inner():
#         # add some additional behavior to decorated function
#         print("I got decorated")

#         # call original function
#         func()
#     # return the inner function
#     return inner

# # define ordinary function
# def ordinary():
#     print("I am ordinary")
    
# # decorate the ordinary function
# decorated_func = make_pretty(ordinary)

# # call the decorated function
# decorated_func()

# # =========================== sau ===========================
# def make_pretty(func):

#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary() 


# def make_pretty(func):
#     def inner(name):
#         print("I got decorated")
#         func(name)
#     return inner

# def ordinary(name):
#     print("I am ordinary, and my name is " + name)
    
# decorated_func = make_pretty(ordinary) # decorated_func = inner

# decorated_func('Atlantis')

# =========================== sau ===========================
# def make_pretty(func):
#     def inner(name):
#         print("I got decorated")
#         func(name)
#     return inner

# @make_pretty
# def ordinary(name):
#     print("I am ordinary, and my name is " + name)

# ordinary("Atlantis") 

# import time

# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time} seconds")
#         return result
#     return wrapper

# @measure_time
# def my_func(*args, **kwargs):
#     nb = 0
#     for i in range(1000000):
#         nb+=i
#     return nb

# print(my_func())


import time


def operation(op_type):
    def measure_time(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Execution time: {end_time - start_time} seconds")
            return result
        return wrapper
    
    if op_type == "measure_time":
        return measure_time
    else:
        raise ValueError("Unsupported operation type")
    

@operation("measure_time")
def my_func(*args, **kwargs):
    nb = 0
    for i in range(1000000):
        nb+=i
    return nb

print(my_func())