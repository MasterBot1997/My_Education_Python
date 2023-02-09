from excep import *
from mod_calc import *
from logg import logging


def menu():
    print("Welcome to menu!\n")
    while True:
        num_type = input("\nEnter\n"
                         "1 - rational calc\n"
                        #  "2 - complex calc\n"
                         "3 - Exit\n")
        match num_type:
            case "1":
                menu_calc()
            # case "2":
            #     menu_calc(num_type)
            case "3":
                logging.info("Stop program")
                print("Thank you for using the calculator, have a nice day!")
                break
            case _:
                logging.warning("Main menu, wrong item selected.")
                print("Error")
                continue


def menu_calc():
    logging.info(f"Start menu calc. With rational.")
    while True:
        rat = input("\nEnter\n"
                           "1 - sum\n"
                           "2 - sub\n"
                           "3 - mul\n"
                           "4 - div\n"
                           "5 - pow\n"
                           "6 - sqrt\n"
                           "0 - back to menu\n")
        
        if rat == "5":
            num_1 = input("Enter number 1: ")
            a = check_data_user(num_1)
        elif rat == "0":
            logging.info('Return menu')
            print("\nReturn menu")
            break
        else:
            num_1 = input("Enter number 1: ")
            a = check_data_user(num_1)
            if rat == "4":
                b = input("Enter number 2: ")
            else:
                num_2 = input("Enter number 2: ")
                b = check_data_user(num_2)
        match rat:
            case "1":
                res = sum(a, b)
                print(f"{a} + {b} = {res}")
                logging.info(f"Div: {a} + {b} = {res}")
            case "2":
                res = sub(a, b)
                print(f"{a} - {b} = {res}")
                logging.info(f"Div: {a} - {b} = {res}")
            case "3":
                res = mul(a, b)
                print(f"{a} * {b} = {res}")
                logging.info(f"Div: {a} * {b} = {res}")
            case "4":
                # Дорабатать знаки
                b = check_number_zero(b)
                c = division_sign()
                res = div(a, b, c)
                print(f"{a} {c} {b} = {res}")
                logging.info(f"Div: {a} {c} {b} = {res}")
            case "5":
                res = pow(a)
                print(f"{a} ** 0.5 = {res}")
                logging.info(f"Div: {a} ** 0.5 = {res}")
            case "6":
                res = sqrt(a, b)
                print(f"{a} ** {b} = {res}")
                logging.info(f"Div: {a} ** {b} = {res}")
            case _:
                logging.warning("Main menu, wrong item selected.")
                print("Error")
                continue

def division_sign():
    while True:
        si = input("\nEnter:"
                    "\n'/'"
                    "\n'//'"
                    "\n'%'\n")
        print(f"Division sign - {si}\n")
        if si == '/' or si == '//' or si == '%':
            match si:
                case '/':
                    return si
                case '//':
                    return si
                case '%':
                    return si
        else:
            logging.warning("Enter division sign error.")
            print("Error division sign!")
            continue
