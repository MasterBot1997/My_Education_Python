# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной
# последовательности в том же порядке.

# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1
# out
# Negative value of the number of numbers!
# []

# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import randint

def new_list(lenghts_list):
    n = []
    for i in range (lenghts_list):
        r = randint(1, 10)
        n.append(r)
    return n

def unique_numbers (lst):
    k = 0
    lst_2 = []
    for i in range(len(lst)):
        if lst.count(lst[i]) < 2:
            lst_2.append(lst[i])
    print(lst_2)

k = int(input("Введте размер количество элементов списка: "))
my_list = new_list(k)
print(my_list)
unique_numbers(my_list)