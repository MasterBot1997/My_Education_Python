# 1. Напишите программу, которая принимает на вход цифру, 
#    обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет


num = int(input("Введите число дня недели от 1 до 7: "))

if num == 6 or num == 7:
    print("Да")
elif 0 < num < 6:
    print("Нет")
else:
    print("Вы ввели число которое не соответствует дню недели")

# if num == 7:
#     print("Воскресенье - выходной")
# elif num == 6:
#     print("Суббота - выходной")
# elif num == 5:
#     print("Пятница")
# elif num == 4:
#     print("Четверг")
# elif num == 3:
#     print("Среда")
# elif num == 2:
#     print("Вторник")
# elif num == 1:
#     print("Понедельник")
# else:
#     print("Вы ввели число которое не соответствует дню недели")