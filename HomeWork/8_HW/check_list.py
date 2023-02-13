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
        with open('data_people.csv', 'r',encoding='utf8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row[filter] == num:
                    return num
            else:
                logging.warning("Введен несуществующий параметр")
                print("\n'Такого параметра не существует!'")
                num = input("Введите еще раз: ")
                print()

# Проверка ключа id для удаления строки с информацией
def check_delite_key(a):
    while True:
        if a.isdigit():
            if int(a) != 0:
                return a
            else:
                logging.warning("Ошбка: id = 0")
                print("\nid не должен быть равен 0!")
                a = input("Введите еще раз: ")
            print()
        else:
            logging.warning("Введен неверный  id")
            print("\nВы ввели некоректный id!")
            a = input("Введите еще раз: ")
            print()