# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн

# in
# 54
# out
# [2, 3, 3, 3]

def natural_multiplier(num):
    lst = []
    while num != 1:
        i = 2
        while num % i != 0:
            i = i + 1
        lst.append(i)
        num = num / i
    print(lst)

natural_multiplier(int(input("Введите число: ")))