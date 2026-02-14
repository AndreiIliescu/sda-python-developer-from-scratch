class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    # Functia __enter__ va fi apelata automat cand ne folosim de cuvantul 'with'
    def __enter__(self):
        # opening the file
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # closing the file
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        self.file.close()

# variabila declarata dupa 'as' isi va lua valoare in functie de
# ce returneaza metoda __enter__
with FileManager('test.txt', 'w') as f:
    f.write('mesaj din file manager')

print('am ajuns la final')
