# Atentie!!!
# problema care poate aparea la angajare!!!
# Codul din finally se va executa mereu, indiferent de ce este scris in try/except

def my_func():
    try:
        return 'a'
    except:
        return 'b'
    finally:
        print('c')

print(my_func())   # se va afisa 'c', indiferent ce se intampla in try sau exception
