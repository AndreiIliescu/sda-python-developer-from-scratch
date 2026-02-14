# try, except, finally
from csv import excel

# Structura
# try:
    # codul pe care incercam sa il rulam
    # si care suspectam ca ar putea avea erori
# except Exception(nume generic pentru exceptii):
    # codul care se executa daca apare o eroare in try
    # Exception este clasa de baza pentru erori
    # poate fi: AttributeError, IndexError, etc
# finally:
    # este optional
    # codul ruleaza la final, indiferent daca am avut o eroare sau nu

# Cazul 1:
# try:
#     a = 5
#     b = 5 / 1
#     assert 4 == 4
#     a.append(10)
# except Exception:               # modul general
#     print('something went wrong!')
# except ZeroDivisionError:       # specific error
#     print('impartit la zero')
# except AssertionError:
#     print('error la assert')
# except AttributeError:
#     print('int nu are append()')

# Cazul 2: daca avem un except care cuprinde mai multe erori
# except (ZeroDivisionError, AssertionError):
#   print('zero div. sau assertion')
# except AttributeError:
#   print('attribute error')
# finally:
#   print('')


# # try, except, else, finally
# try:
#     # cod care poate genera eroare
# except SomeError:
#     # tratarea erorii
# else:
#     # cod care se execută doar dacă în blocul try NU s-a produs nicio excepție
# finally:
#     # cod care se execută întotdeauna, indiferent dacă a apărut sau nu excepția
# Exemplu 1:
# try:
#     x = 5 / 1
# except ZeroDivisionError:
#     print("Împărțire la zero!")
# else:
#     print("Împărțire realizată cu succes!")
# finally:
#     print("Acest cod se execută întotdeauna.")

# Exemplu 2:
# except Exception -> cazul general care prinde toate erorile
try:
    f = open('file.txt')
    print(f.read())
except Exception:
    print('Eroare la deschis fisier')

# Exemplu 3:
x = 5
my_list = [1,0,2]

for elem in my_list:
    try:
        result = x / elem
    except ZeroDivisionError:
        print('Nu poti imparti la 0.')

        # in cazulm unei erori trece mai departe in for
        # sarim peste eroare
        continue
    print(f'Result is {result}')
# Se va afisa:
# Result is 5.0
# Nu poti imparti la 0.
# Result is 2.5
