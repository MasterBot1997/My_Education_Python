# Все типы операций для рациональных чисел
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

# Всее типы операций для комлексных чисел

def sum_comp(a, b, c, d):
    res1 = a + c
    res2 = b + d
    if res1 == 0:
        return f"{res2}j"
    elif res2 == 0:
        return f"{res1}"
    elif res1 == 0 and res2 == 0:
        return 0
    elif res2 < 0:
        res2 = res2 * -1
        return f"{res1} - {res2}j"
    else:
        return f"{res1} + {res2}j"


def sub_comp(a, b, c, d):
    res1 = a - c
    res2 = b - d
    if res1 == 0:
        return f"{res2}j"
    elif res2 == 0:
        return f"{res1}"
    elif res1 == 0 and res2 == 0:
        return 0
    elif res2 < 0:
        res2 = res2 * -1
        return f"{res1} - {res2}j"
    else:
        return f"{res1} + {res2}j"


def mul_comp(a, b, c, d):
    res1 = a*c - b*d
    res2 = b*c + a*d
    if res1 == 0:
        return f"{res2}j"
    elif res2 == 0:
        return f"{res1}"
    elif res1 == 0 and res2 == 0:
        return 0
    elif res2 < 0:
        res2 = res2 * -1
        return f"{res1} - {res2}j"
    else:
        return f"{res1} + {res2}j"


def div_comp(a, b, c, d):
    res1 = round(((a*c+b*d)/(c**2 + d**2)), 4)
    res2 = round(((b*c-a*d)/(c**2 + d**2)), 4)
    if res1 == 0:
        return f"{res2}j"
    elif res2 == 0:
        return f"{res1} + j"
    elif res2 < 0:
        res2 = res2 * -1
        return f"{res1} - {res2}j"
    else:
        return f"{res1} + {res2}j"