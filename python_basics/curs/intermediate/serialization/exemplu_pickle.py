import pickle

data = {
    'a': [1, 4.5, 100, 45.34],
    'b': ('Ana are mere', 'Python is cool'),
    'c': True,
}

# Important! Accesam fisierele si cu modul 'b' (binary)
# Pentru ca pickle salveaza datele in format binar
# f = open('data.pickle', 'wb')
# pickle.dump(data, f)
# f.close()
# SAU
with open('data.pickle', 'wb') as f:
    # Scriem datele in fisier
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    # Citim datele din fisier
    loaded_data = pickle.load(f)
    print(loaded_data)


# var1=ceva_valoare
