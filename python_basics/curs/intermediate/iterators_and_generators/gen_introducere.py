### Generatori ###
# Exemplu 1
def my_generator():
    a = 1
    print('am intract in gen', a)

    # 'yield' va 'ingheta' functia in stadiul in care este
    # functia my_generator() se continua cand apelam pe ea next()
    yield

    print('din nou in gen', a)

    yield

    print('a treia oara', a)

gen = my_generator()
next(gen)
print('in codul principal')
next(gen)
# next(gen)

print('\n\n')

# Exemplu 2
def even_generator(n):
    current_number = 2
    generated_count = 0

    while generated_count < n:
        yield current_number

        current_number += 2
        generated_count += 1

# even_numbers = even_generator(10)
# print(next(even_numbers))
# print(next(even_numbers))
# print(next(even_numbers))

even_numbers = even_generator(10)
for n in even_numbers:
    print(n)
