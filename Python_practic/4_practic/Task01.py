# 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

def user_input (user_str):
    new_str = user_str.split()
    list = []

    for i in range(len(new_str)):
        new_str[i] = new_str[i].replace("-", " ", 1).strip(",;!")
        if new_str[i].isdigit():
            list.append(new_str[i])
    return list

def user_output(list):
    if list:
        return max(list, key=int), min(list, key=int)
    return"error"

print(user_output(user_input(input("..."))))
