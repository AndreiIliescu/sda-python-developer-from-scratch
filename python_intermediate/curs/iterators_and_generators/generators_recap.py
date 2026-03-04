from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# def get_n_primes(n):
#     primes = []
#     i = 2
#     while len(primes) != n:
#         if is_prime(i):
#             primes.append(i)
#         i += 1
#     return primes

# lst = get_n_primes(1_000_000)
# lst = get_n_primes(50_000)
# print(lst)
# for elem in lst:
#     print(elem)


# def prime_generator(n):
#     # Generator for iterating over n primes
#     number = 2
#     generated_numbers = 0
#     while generated_numbers != n:
#         if is_prime(number):
#             yield number # se iese din functie, se returneaza valoarea si se va continua de aici la urmatoarea iteratie
#             generated_numbers += 1
#         number += 1


# gen = prime_generator(50_000)
# gen = prime_generator(1_000_000)

# gen = prime_generator(3)
# print(gen)
# # print(next(gen)) # primul nr din generator
# # print(next(gen)) # al doilea nr din generator
# # print(next(gen))
# # print(next(gen)) # eroare: generatorul a ajuns la capat

# for elem in gen: # for-ul merge pana la capat 
#     print(elem)

class PrimeIterator:
    # Iterator that allows you to iterate over n primes
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self): # da regula de iterare
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()
    

# iter = PrimeIterator(1_000_000)
iter = PrimeIterator(1_000)

for elem in iter:
    print(elem)



# chain of responsability:
# p1 = Process_1()
# p2 = Process_2()
# p3 = Process_3()

# p1.next_process = p2
# p2.next_process = p3
# p1.process()

