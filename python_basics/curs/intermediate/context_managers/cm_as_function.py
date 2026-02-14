from contextlib import contextmanager

@contextmanager
def file_manager_func(name, mode):
    # Cod echivalent cu functia __enter__ (daca am folosi o clasa pt CM)
    f = open(name, mode)
    print('am intrat in context')

    # Echivalent cu valoare returnata de functia __enter__
    yield f

    # Echivalent cu functia __exit__
    print('am iesit din context')
    f.close()

with file_manager_func('test.txt', 'w') as f:
    f.write('context manager ca si functie')
