# 4. Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.

num = float(input("Введите дробное число: "))
new_num = int(num * 10 % 10)
print("")
print(new_num)