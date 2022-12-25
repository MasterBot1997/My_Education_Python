# 5. Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве. 
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
print("Введите значения координат точки А(X1, Y1)")
x1 = int(input("Введите значение X1: "))
y1 = int(input("Введите значение Y1: "))

print("Введите значения координат точки B(X2, Y2)")
x2 = int(input("Введите значение X2: "))
y2 = int(input("Введите значение Y2: "))

from math import sqrt
rangeX = x1 - x2
rangeY = y1 - y2
# result = (rangeX * rangeX + rangeY * rangeY) ** 0.5
result = round(sqrt(rangeX * rangeX + rangeY * rangeY), 2)

# print(f"Расстояние между точками A({x1},{y1}) и В({x2},{y2}) равно {result:.2f}")
print(f"Расстояние между точками A({x1},{y1}) и В({x2},{y2}) равно {result}")