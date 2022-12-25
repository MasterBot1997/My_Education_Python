# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

n = float(input("Введите вещественное исло: "))
size_n = len(f'{n}')
m = n * 10 ** size_n
count = 0

# i = 0
# while i <= size_n:
#     m = int(m / 10)
#     print(m)
#     z = m % 10
#     print(z)
#     count = count + z
#     print(count)
#     i+=1 

for i in range(size_n + 1):
    m = int(m / 10)
    z = m % 10
    count = count + z

print(count)