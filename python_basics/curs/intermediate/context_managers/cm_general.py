### Context Managers ###

# Exemplu de context manager din python cu 'with'
# f = open('test.txt', 'w')
# f.write('text scris in fisier')
# f.close()
# Echivalent cu a scrie:
# with open('test.txt', 'w') as f:
#   f.write('text scris in fisier')

class MyContextManager:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('am intrat in context')
        print(f'name is {self.name}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('am iesit din context')

with MyContextManager('First CM'):
    print('se executa niste cod')

print('Am ajuns la final')
