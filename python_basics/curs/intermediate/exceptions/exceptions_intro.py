# ZeroDivisionError
# atunci cand impartim un numar cu 0, indiferent de context
#print(5 / 0)       # ZeroDivisionError: division by zero

# AssertionError
# atunci cand conditia din assert este False
# a = 3
# b = 2
# assert a == b     # AssertionError

# AtributeError
# cand incercam sa accesam un atribut/apelam o metoda care nu exista pe un obiect
# x = 10
# x.append(8)       # AttributeError: 'int' object has no attribute 'append'

# FileNoFoundError
# atunci cand incercam sa deschidem un fisier care nu exista
# f = open('file.txt')
# print(f.read())       # FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'

# IndexError
# atunci cand accesam un element dintr-o lista cu un index care nu exista
# my_list = [1,2,3]
# print(my_list[10])      #IndexError: list index out of range

# ImportError
# daca importam o functie care nu exista
# from sys import no_exist      # ImportError: cannot import name 'no_exist' from 'sys' (unknown location)

# ModuleNotFoundError
# daca importam un modul care nu exista sau care nu este instalat
#import pygame      # ModuleNotFoundError: No module named 'pygame'

# KeyError
# atunci cand citim o cheie care nu exista intr-un dictionar
# people = {
#     "Ion": 100,
#     "Ana": 50,
# }
# print(people['Ion'])
# print(people['Mircea'])     # KeyError: 'Mircea'

# NameError
# daca folosim o variabila nedeclarata
# a = 10
# c = a + b       # NameError: name 'b' is not defined

# TypeError
# atunci cand operam pe tipuri de date incompatibile
# 1 + 'a'     # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ValueError
# cand trimitem un parametru gresit unei functii
# a = 'un string'
# b = int(a)
# print(b)        # ValueError: invalid literal for int() with base 10: 'un string'

# # IndentationError
# Apare când indentarea codului nu este corectă.
# Ex: lipsă spații sau taburi în mod greșit.

# SyntaxError
# Când codul nu e sintactic corect (greșeli de scriere).

# StopIteration
# Apare când un iterator ajunge la final și nu mai are elemente.

# RuntimeError
# Eroare generală la runtime, când altceva neașteptat se întâmplă.

# OverflowError
# Când un calcul numeric depășește limita maximă permisă.

# MemoryError
# Când Python nu mai are memorie pentru alocații.

# RecursionError
# Când o recursie depășește adâncimea maximă permisă (recursie infinită).

# StopAsyncIteration
# Similar cu StopIteration, dar pentru iteratoare asincrone.
