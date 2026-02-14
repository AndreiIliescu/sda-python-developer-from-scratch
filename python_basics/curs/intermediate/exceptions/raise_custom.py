# cuvantul 'raise' care va 'ridica' o eroare
# eroarea poate opri programul sau 'handled' intr-un try/except


# Sintaxa:
# raise ValueError('mesajul erorii') # trimite o eroare cu mesajul specificat

# Exemplu simplu pentru 'raise'
# def my_func(my_list):
#     x = 3
#     for elem in my_list:
#         if elem == 0:
#             raise ValueError('Atentie! Un element din lista este 0')
#
#         result = x / elem
#         print(f'Result is {result}')
#
#
# my_func([1,0,2])

# Se va afisa:
# Result is 3.0
# Traceback (most recent call last):
#   File "C:\Users\olimp\PycharmProjects\Pythonremote76\curs\intermediate\exceptions\raise_custom.py",
#   line 18, in <module>
#     my_func([1,0,2])
#     ~~~~~~~^^^^^^^^^
#   File "C:\Users\olimp\PycharmProjects\Pythonremote76\curs\intermediate\exceptions\raise_custom.py",
#   line 12, in my_func
#     raise ValueError('Atentie! Un element din lista este 0')
# ValueError: Atentie! Un element din lista este 0


# Pentru a creea tipuri noi de erori:

# Varianta 1:
# class CustomException(Exception):
#     pass
# raise CustomException
# Se va afisa:
#     raise CustomException
# CustomException

# Varianta 2:
# class EvenDivisionException(Exception):
#     def __init__(self):
#         message = 'Nu poti imparti cu un nr. par'
#         super().__init__(message)
# raise EvenDivisionException

# Se va afisa:
#  raise EvenDivisionException
# EvenDivisionException: Nu poti imparti cu un nr. par
