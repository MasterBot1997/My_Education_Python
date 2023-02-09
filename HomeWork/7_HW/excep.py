from logg import logging

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
                return "Error data"
        else:            
            logging.warning("Incorrect data entered!")
            print("\n'Error data number!'")
            x = input("Restart number: ")


def check_number_zero(num):
    while True:
        num = check_data_user(num)
        if num == 0:
            print("Error second value. Check if it's 0.\n")
            num = input("Enter number 2: ")
        else:
            return num