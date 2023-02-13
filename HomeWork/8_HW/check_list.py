from logg import logging
import csv
# Проверка является ли id первым или нет, на слуай нового списка
def check_last_id(num):
    if num.isdigit():
        logging.info(f"Последний id - {num}")
        return int(num)
    else:
        logging.info("Это первая запись данных о пользователе id - 1")
        num = 0
        return int(num)

# Проверка корректности ввода ключа, для полчучения данных о 
# пользователе через id
def check_key(filter, num):
    while True:
        with open('data_people.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row[filter] == num:
                    return num
            else:
                logging.warning("Введен несуществующий параметр")
                print("\n'Такого параметра не существует!'")
                num = input("Введите еще раз: ")
                print()

