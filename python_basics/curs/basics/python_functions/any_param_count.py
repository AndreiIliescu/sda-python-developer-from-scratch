def some_function(a, b, c, *args, x='abc', y=True, z=None, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(args, type(args))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(kwargs, type(kwargs))

some_function(1, 2, 3, 5, 6, 7, x='cde', y=False, z=True, x1='cde', x2='kjsdhf')
