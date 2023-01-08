# 1. Задайте список, состоящий из произвольных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).

# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import randint

def new_list(lenghts_list):
    n = []
    for i in range (lenghts_list):
        r = randint(1, 20)
        n.append(r)
    return n

def sum_pos(spisok):
    count = 0
    for i in range(0, len(spisok), 2):
        count += + spisok[i]
    return count

k = int(input("Введте размер количество элементов списка: "))
my_list = new_list(k)
print(my_list)
need_sum = sum_pos(my_list)
print(need_sum)
