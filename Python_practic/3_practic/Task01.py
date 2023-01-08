# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая определит, присутствует ли в заданном списке число,
# полученное от пользователя.

# from random import randint
# from random import sample

# n = []
# k = int(input("Введте размер количество элементов списка: "))
# number = int(input())

# for i in range (k):
#     r = randint(1, 10)
#     n.append(r*2)
# print (n)

# if number in n:
#     print('Yes')
# else:
#     print('No')

from random import sample

def num_find (len_list, number):
    new_list = sample (range (1, len_list * 2), k=len_list)
    print(new_list)
    if number in new_list:
        return 'Yes'
    return 'No'

print (num_find (int (input('Введите длину списка -')), int (input('Введите число -'))))