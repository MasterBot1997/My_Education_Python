def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b, c):
    if c == '/':
        return round(a / b, 2)
    elif c == '//':
        return round(a // b, 2)
    else:
        return round(a % b, 2)


def pow(a):
    return round(a ** 0.5, 2)


def sqrt(a, b):
    return a ** b
