from logg import logging
from mod_file import *
import csv
# Меню:
# - Показать все записи,
# - Найти запись,
# - Добавить запись,
# - Редактировать запись,
# - Удалить запись,
# - Экспорт/Импорт
# - Выход


def menu():
    logging.info("Программа запущенна.")
    print("Welcome to menu!")
    while True:
        id_last = last_id()
        # Выбор пользователя какой действие он хочет выполнить
        num_type = input("\nEnter\n"
                         "1 - Показать записи\n"
                         "2 - Найти записи\n"
                         "3 - Добавить записи\n"
                         "4 - Редактировать записи\n"
                         "5 - Удалить записи\n"
                         "6 - Экспорт/Ипорт\n"
                         "0 - Завершение программы\n")
        match num_type:
            case "1":
                print_file()
            case "2":
                # Пользователь вводит id что бы проверить какая есть информация по этому id
                prin_dict_menu()
            case "3":
                new_entry(id_last)
            case "4":
                break
            case "5":
                break
            case "6":
                break
            case "0":
                logging.info("Завершение программы.")
                print("\nСпасибо, что пользуетесm нашим приложением!\nХорошего вам дня!")
                break
            case _:
                logging.warning("Пользователь ввел некоректное значение!")
                print("Такого варанта нет, попробуйте еще раз!")
                continue


def prin_dict_menu():
    while True:
        name_key = input("Ввдеите по какому параетру вы хотите вывести иформацию: \n"
                        "1 - id\n"
                        "2 - Name\n"
                        "3 - Last_name\n"
                        "4 - Start_work\n"
                        "5 - job_title\n"
                        "6 - number_phone\n"
                        "0 - Вернуться в меню\n")
        match name_key:
            case '1':
                key_user = input("Введите id сотрудника: ")
                print()
                filter_user = "id"
                prin_dict(filter_user, key_user)
                break
            case '2':
                key_user = input("Введите Имя сотрудника: ")
                print()
                filter_user = "Name"
                prin_dict(filter_user, key_user)
                break
            case '3':
                key_user = input("Введите Фамилию сотрудника: ")
                print()
                filter_user = "Last_name"
                prin_dict(filter_user, key_user)
                break
            case '4':
                key_user = input("Введите дату начала работы сотрудника: ")
                print()
                filter_user = "Start_work"
                prin_dict(filter_user, key_user)
                break
            case '5':
                key_user = input("Введите должность сотрудника: ")
                print()
                filter_user = "job_title"
                prin_dict(filter_user, key_user)
                break
            case '6':
                key_user = input("Введите номер телефона сотрудника: ")
                print()
                filter_user = "number_phone"
                prin_dict(filter_user, key_user)
                break
            case '0':
                logging.info("Возвращение в меню")
                print("\nВы возвращаетесь в меню\n")
                menu()
            case _:
                logging.warning("Пользователь ввел некоректное значение!")
                print("Такого варанта нет, попробуйте еще раз!")
                continue