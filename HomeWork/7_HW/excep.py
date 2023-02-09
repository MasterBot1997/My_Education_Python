from logg import logging

# Проверка Входного числа и присвоение числу типа данных
def check_data_user(x):
    while True:
            if x != '':
                if x.isnumeric() or x.replace("-","").isdigit():
                    return int(x)
                elif x.count(".") == 1:
                    return float(x)
                elif x.count(".") == 1 and x.replace("-", "").replace(".", "").isdigit():
                    return float(x)
                else:            
                    logging.warning("Incorrect data entered!")
                    print("\n'Error data number!'")
                    x = input("Restart number: ")
            else:            
                    logging.warning("Incorrect data entered!")
                    print("\n'Error data number!'")
                    x = input("Restart number: ")

# Проверка знаминателля при делениии рациональных чисел
def check_number_zero(num):
    while True:
        num = check_data_user(num)
        if num == 0:
            print("Error second value. Check if it's 0.\n")
            num = input("Enter number 2: ")
        else:
            return num


# def check_number_zero_comp(num_1, num_2):
#     while True:
#         if num_1 == "0" and num_2 == "0":
#             press = input("\nОба числа равны 0. Выберете число которое введете заново"
#                           "\n1 - number 3"
#                           "\n2 - number 4")
#         match press:
#             case "1":
#                 num_1 = input("Enter number 3: ")
#             case "2":
#                 num_2 = input("Enter number 4: ")
        