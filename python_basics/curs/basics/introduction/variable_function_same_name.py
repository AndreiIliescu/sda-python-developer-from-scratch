import time

t1 = time.time()

a = 0

print(type(a))

def a():
    pass

print(type(a))

a = True

print(type(a))

def a(x, y, z):
    pass

print(type(a))

time.sleep(4)

t2 = time.time()

print(f'{t2 - t1} seconds elapsed.')
