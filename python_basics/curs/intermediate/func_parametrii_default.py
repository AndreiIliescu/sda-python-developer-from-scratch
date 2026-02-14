# Default parameters
def show_message(message='default message'):
    print(f'My message is {message}')

# Functie show_message() are pentru parametrul message o valoare default
# Daca apelam functia fara a specifica valori noi
# Ea va folosi valoarea default
show_message()

# Daca apelam functia cu alta valoarea, ea va inlocui valoarea default
show_message('alt mesaj')
