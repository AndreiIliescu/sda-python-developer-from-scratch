def add(*args) -> int:
    print(type(args))
    result = 0
    for arg in args:
        result += arg
    return result


print(add(1, 11, 21, 35, 67))
