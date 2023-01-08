# 3. Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011


def binary_number (num):
    n = []
    while num:
        n.append(num % 2)
        num = int(num / 2)
    return n

number = int(input('Введите десятичное число: '))
my_list = binary_number(number)
my_list.reverse()
print(my_list)