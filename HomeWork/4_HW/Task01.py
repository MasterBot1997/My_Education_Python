# 1. Вычислить число c заданной точностью d

# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

from decimal import Decimal

n = float(input("Введите число: "))
print("Введите до какой точности хотите проверить число. Пример: d = 1.00\nПримечание: количество чисел после еденицы обозначает точность округления числа")
d = input()

# Попроровал сделать проверку, но для это d надо было сделать float типом, из за
# этого возникает ошибка, и число для которого проверяется точность не срабатывает.
# d = float(input())
# if 1 <= d < 2:
#     number = Decimal(n)
#     number = number.quantize(Decimal(d))
#     print(number)
# else:
#     print("Некорректно введена точность!")

number = Decimal(n)
number = number.quantize(Decimal(d))
print(number)