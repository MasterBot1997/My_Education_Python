from excep import *
from mod_calc import *
from logg import logging


def menu():
    print("Welcome to menu!\n")
    while True:
        num_type = input("\nEnter\n"
                         "1 - rational calc\n"
                         "2 - complex calc\n"
                         "3 - Exit\n")
        match num_type:
            case "1":
                menu_calc()
            case "2":
                menu_calc_comp()
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

def menu_calc_comp():
    logging.info(f"Start menu calc. With complex.")
    while True:
        rat = input("\nEnter\n"
                    "1 - sum\n"
                    "2 - sub\n"
                    "3 - mul\n"
                    "4 - div\n"
                    "0 - back to menu\n")

        if rat == "0":
            logging.info('Return menu')
            print("\nReturn menu")
            break
        else:
            num_1 = input("Enter number 1: ")
            a = check_data_user(num_1)
            num_2 = input("Enter number 2: ")
            b = check_data_user(num_2)
            if rat == "4":
                # Не совсем понял как правильно записать функцию проверки 0
                # в знаминателе для комплексных чисел, поэтому она тут
                num_3 = input("Enter number 3: ")
                num_4 = input("Enter number 4: ")
                if num_3 == "0" and num_4 == "0":
                    logging.info("Both numbers are 0.")
                    while True:
                        press = input("\nОба числа равны 0. Выберете число которое введете заново"
                                    "\n1 - number 3"
                                    "\n2 - number 4\n")
                        match press:
                            case "1":
                                num_3 = input("Enter number 3: ")
                                logging.info(f"Number 3 was changed to {num_3}")
                                if num_3 != "0":
                                    c = check_data_user(num_3)
                                    break
                            case "2":
                                num_4 = input("Enter number 4: ")
                                logging.info(f"Number 3 was changed to {num_4}")
                                if num_4 != "0":
                                    c = check_data_user(num_4)
                                    break
                            case _:
                                logging.warning("Main menu, wrong item selected.")
                                print("Error")
                                continue
                else:
                    c = check_data_user(num_3)
                    d = check_data_user(num_4)
            else:
                num_3 = input("Enter number 3: ")
                c = check_data_user(num_3)
                num_4 = input("Enter number 4: ")
                d = check_data_user(num_4)
        match rat:
            case "1":
                res = sum_comp(a, b, c, d)
                print(f"({a} + {b}j) + ({c} + {d}j) = {res}")
                logging.info(f"Sum_complex: ({a} + {b}j) + ({c} + {d}j) = {res}")
            case "2":
                res = sub_comp(a, b, c, d)
                print(f"({a} + {b}j) - ({c} + {d}j) = {res}")
                logging.info(f"Sub_complex: ({a} + {b}j) - ({c} + {d}j) = {res}")
            case "3":
                res = mul_comp(a, b, c, d)
                print(f"({a} + {b}j) * ({c} + {d}j) = {res}")
                logging.info(f"Sub_complex: ({a} + {b}j) * ({c} + {d}j) = {res}")
            case "4":
                res = div_comp(a, b, c, d)
                print(f"({a} + {b}j) / ({c} + {d}j) = {res}")
                logging.info(f"Div_complex: ({a} + {b}j) / ({c} + {d}j) = {res}")
            case _:
                logging.warning("Main menu, wrong item selected.")
                print("Error")
                continue