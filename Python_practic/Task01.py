# Напишите программу которая принимает на вход 2 числа и
# проверяет, являетс ли одно число квадратом второго.


n = int(input())
m = int(input())

if n == m**2 or m == n**2:
    print("Yes")
else:
    print("No")