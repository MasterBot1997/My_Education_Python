# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.

# in                              out
# 9                               [15, 16, 2, 3, 1, 7, 5, 4, 10]
#                                 [16, 3, 7, 10]

# in                              out
# 10                              [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
#                                 [24, 15, 23, 25]

from random import randint

n = int(input("Введите размер спписка: "))
lst = [randint(1,50) for i in range(n)]
lst2 = [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]
print(lst)
print(lst2)