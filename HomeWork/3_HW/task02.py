# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

from random import randint


def new_list(lenghts_list):
    n = []
    for i in range(lenghts_list):
        r = randint(1, 20)
        n.append(r)
    return n


def new_list_2(list):
    n_2 = []
    if int(len(list) % 2) == 0:
        for i in range(int(len(list) / 2)):
            n_2.append(list[i] * list[len(list) - i - 1])
    else:
        for i in range(int(len(list) / 2) + 1):
            if i != int(len(list) / 2):
                n_2.append(list[i] * list[len(list) - i - 1])
            else:
                n_2.append(list[i])
    return n_2


k = int(input("Введте какое будет количество элементов списка: "))
my_list = new_list(k)
print(my_list)
my_list_2 = new_list_2(my_list)
print(my_list_2)