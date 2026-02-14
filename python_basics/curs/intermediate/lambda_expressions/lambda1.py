### Lambda expressions ###

# Functille lambda sunt functii anonime (nu le declaram cu 'def' uramat de un nume)
# ex: lambda x: scurt cod care face o operatiune cu x
# x este parametru functiei
# codul pus dupa ':' va fi returnat de functie

# Exemplu 1
my_lambda = lambda x: x.lower()
print(my_lambda('HELLO WORLD!'))

# Codul de mai sus este echivalent cu
# def my_lambda(x):
#     return x.lower()

# Exemplu 2
square_lambda = lambda a: a ** 2
print(square_lambda(4))

# Exemplu 3
equals_lambda = lambda x, y: x == y
print(equals_lambda(3, 3))
