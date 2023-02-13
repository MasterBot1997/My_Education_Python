import csv
from check_list import *


# печать файла в консоль
def print_file():
    with open('data_people.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# Новые данные от пользователя
def new_entry(num):
    row = []
    num = num + 1
    with open('data_people.csv', 'a', newline='') as f:
        a = input('Введите новые данные через пробел: ')
        row.append(num)
        for i in range(len(a.split())):
            row.append(a.split()[i])
        writer = csv.writer(f)
        writer.writerow(row)



# Оппределение последнего id
def last_id():
    with open('data_people.csv') as f:
        g = f.readlines()[-1].split(',')
        c = g[0]
        b = check_last_id(c)
        return(b)

# функция вывода данных сотрудника с определенным id, реализовано через словарь
def prin_dict(filter, key):
    key = check_key(filter, key)
    with open('data_people.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row[filter] == key:
                print(row['id'],row['Name'], row['Last_name'],row['Start_work'], row['job_title'], row['number_phone'])