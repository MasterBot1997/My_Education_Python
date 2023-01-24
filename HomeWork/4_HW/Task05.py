from random import choice, sample

# Метод создания файла с многочленом
def polynomial(num: int, name):
    if num < 1:
        return 0

    poly = ""
    num_list = range(0, 11)

    with open(name, "a", encoding="utf-8") as my_f:
        for i in range(num, 1, -1):
            value = choice(num_list)
            if value:
                poly += f"{value}*x^{i} {choice('+-')} "    
        numbers = sample(range(1, 11), k=2)
        my_f.write(f"{poly}{choice(numbers)}*x {choice('+-')} {choice(numbers)} = 0\n")

# Метод сложения многочленов из двух файлов
def poly_sum(name_1: str, name_2: str):
    with open(name_1, "r", encoding="utf-8") as my_f_1, \
            open(name_2, "r", encoding="utf-8") as my_f_2:
        first = my_f_1.readlines()
        second = my_f_2.readlines()

    if len(first) == len(second):
        with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
            for i, v in enumerate(first):
                my_f_3.write(f"{v[:-5]} + {second[i]}")
    else:
        print("The contents of the files do not match!")

# Циклы где мы задаем имя файла и количество символов
for _ in range(2):
    name_file = str(input())
    for _ in range(3):
        polynomial(int(input()), name_file)

# poly_sum(input("Enter the file name 'text_1.txt': "), input("Enter the file name 'text_2.txt': "))
poly_sum("poly.txt", "poly_2.txt")