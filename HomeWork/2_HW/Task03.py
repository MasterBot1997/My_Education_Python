# 3. Задайте список из n чисел, заполненный 
# по формуле (1 + 1/n) ** n и выведите на экран их сумму.

# in 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

n = []
k = int(input("Введите до "))
count = 0
for i in range (1, k + 1):
    n.append(round((1 + 1 / i) ** i, 3))
    count = count + round((1 + 1 / i) ** i, 3)
print (n)
print(count)