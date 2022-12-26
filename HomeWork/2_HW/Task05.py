# 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randint

n = []
k = int(input("Введте размер количество элементов списка: "))

for i in range (k):
    n.append(i)
print (n, '<-- not mixed')

for i in range (k):
    r = randint(i,k - 1)
    m = n[i]
    n[i] = n[r]
    n[r] = m
print(n, '<-- mixed')