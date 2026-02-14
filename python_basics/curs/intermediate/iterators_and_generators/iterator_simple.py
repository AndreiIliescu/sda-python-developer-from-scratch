### Iterators ###
# Functia iter() transforma o lista intr-un iterator
# Putem parcurge un iterator intr-un for
# SAU folosind functia next()
my_iter = iter([8, 9, 30, 20])

# for elem in my_iter:
#     print(elem)

print(next(my_iter))
print(next(my_iter))

# niste cod mai mult

print(next(my_iter))
print(next(my_iter))

# Eroare! Nu putem accesa date din iterator ca dintr-o lista
# print(my_iter[0])
