from logg import logging

# Меню:
# - Показать все записи,
# - Найти запись,
# - Добавить запись,
# - Редактировать запись,
# - Удалить запись,
# - Экспорт/Импорт
# - Выход


def menu():
    print("Welcome to menu!\n")
    while True:
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
                break
            case "2":
                break
            case "3":
                break
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