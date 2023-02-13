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
def check_key(num):
    while True:
        with open('data_people.csv') as f:
            reader = csv.DictReader(f)
            if num.isdigit():
                for row in reader:
                    if row['id'] == num:
                        return num
                else:
                    logging.warning("Введен несуществующий id")
                print("\n'Такого id не существует!'")
                num = input("Введите id еще раз: ")
            else:
                logging.warning("Неверно введен id!")
                print("\n'Неверно введен id!'")
                num = input("Введите id еще раз: ")