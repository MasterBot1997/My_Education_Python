# 4. Задайте список из произвольных вещественных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

from random import uniform


def new_list(lenghts_list):
    n = []
    for i in range(lenghts_list):
        r = uniform(1, 10)
        n.append(round(r, 2))
    return n

def min_num(list):
    min = list[0] % 1
    for i in range (1, len(list)):
        if min > list[i] % 1:
            min = list[i] % 1
    return min

def max_num(list):
    max = list[0] % 1
    for i in range (1, len(list)):
        if max < list[i] % 1:
            max = list[i] % 1
    return max

def difference (max_n, min_n):
    dif = max_n - min_n
    dif = round(dif, 2)
    print(f'Difference: {dif}')

k = int(input("Введте какое будет количество элементов списка: "))
my_list = new_list(k)
print(my_list)
min_number = min_num(my_list)
min_number = round(min_number, 2)
print(f'Минимальная дробная часть числа в списке = {min_number}')
max_number = max_num(my_list)
max_number = round(max_number, 2)
print(f'Максимальная дробная часть числа в списке = {max_number}')
difference(max_number, min_number)