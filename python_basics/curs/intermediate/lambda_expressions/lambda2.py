# Aplicatiile functiilor lambda
# map, filter, reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
# codul clasic pentru a crea o lista cu elementele dublate
# doubled = []
# for x in numbers:
#    doubled.append(x * 2)

# Functia map() ia ca parametrii o functie lambda care descrie operatiunea aplicata pe elementele din lista
# si lista pe care se va aplica operatiunea
# map() returneaza o lista noua
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Functiile lambda sunt foarte rapide
# numbers = range(50000000)
# from curs.intermediate.context_managers.cm_timer import TimeIt
# with TimeIt():
#     print('Time for lambda')
#     doubled = map(lambda x: x * 2, numbers)
#
# with TimeIt():
#     print('Time for for loop')
#     doubled = []
#     for x in numbers:
#        doubled.append(x * 2)

# filter() ia parametrii
# o functie lambda care returneaza True / False
# lista pe care aplicam operatia
odd_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(odd_numbers)

# reduce() va returna o singura valoare
# numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)
