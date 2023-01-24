# 2. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.

from random import choices

def FillList():
    n = int(input("Введите длину списка: "))
    my_list = choices(range(n * 2), k=n)
    return my_list

def SortList(s_list):
    new_list = []
    for i in range(len(s_list)):
        temp = s_list[i]
        d_list = [temp]
        for j in range(i + 1, len(s_list)):
            if s_list[j] > temp:
                temp = s_list[j]
                d_list.append(temp)
        if len(d_list) > 1:
            new_list.append(d_list)
    return new_list

a = FillList()
print(a)
print()
print(SortList(a))