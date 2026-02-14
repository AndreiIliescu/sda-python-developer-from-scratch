from datetime import datetime

def disable_at_night_with_params(from_, to_):
    # Daca avem parametrii in decorator
    # Avem nevoie de doua functii in interiorul lui
    # In acest caz functia dec(func) ia parametrul func care este functia originala
    def dec(func):
        def wrapper(*args, **kwargs):
            print(f'Valoarea args din functia originala: {args}')
            print(f'Valoarea kwargs din functia originala: {kwargs}')
            if from_ <= datetime.now().hour < to_:
                func(*args, **kwargs)

        return wrapper

    return dec

@disable_at_night_with_params(20, 22)
def say_something():
    print('Hello World!')

@disable_at_night_with_params(20, 22)
def print_message(msg, extra_message):
    print(msg)

say_something()
print_message('hi from func with args', extra_message='mesaj kwargs')
