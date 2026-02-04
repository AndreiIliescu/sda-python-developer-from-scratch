def draw_triangle(size):
    s = size
    x = int(size * 2)
    tmp = ' ' * x
    for i in range(s):
        t = list(tmp)
        t[s - i] = '#'
        t[s + i] = '#'
        print(''.join(t))
    print('#' * (x + 1))


def draw_circle(size):
    radius = size / 2 - 0.5
    for i in range(size):
        y = (1 - radius) ** 2
        line = ""
        for j in range(size):
            x = (j - radius) ** 2
            if abs(x + y - radius ** 2) < radius:
                line += "#"
            else:
                line += " "
        print(line)


def draw_rectangle(size1, size2):
    for i in range(size1):
        print("#" * size2)


def draw_square_diagonel_prime(size):
    for i in range(size):
        if i == 0 or i == size - 1:
            print('#' * size)
        else:
            new_line = '#' + ' ' * (size - 2) + '#'
            new_line = list(new_line)
            #print(new_line)
            #print()
            # new_line[i] = '#'
            new_line[size - 1 - i] = '#'
            #print(new_line)
            #print()
            new_line = ''.join(new_line)
            print(new_line)


def print_menu():
    print('1. Triangle')
    print('2. Rectangle')
    print('3. circle')
    print('4. square')
    print('x. Exit')


def main():
    print_menu()
    command = input('Introduceti o comanda:')
    while command != 'x':
        match (command):
            case '1':
                size = int(input("Triangle size:"))
                draw_triangle(size)
            case '2':
                size1 = int(input("Rectangle size1: "))
                size2 = int(input("Rectangle size2: "))
                draw_rectangle(size1, size2)

            case '3':
                diameter = int(input("diametrul cercului:"))
                draw_circle(diameter)

            case '4':
                size = int(input('latura patrat: '))
                draw_square_diagonel_prime(size)
            case _:

                print("invalid command!")

        print_menu()
        command = input('Introduceti o comanda:')

    print('Thank you, goodbye!')

print('This will always be visible.')
print(f'__name__={__name__}')
if __name__ == '__main__':
    # print('This program will draw shapes.')
    main()

# if __name__ == '__main__':
