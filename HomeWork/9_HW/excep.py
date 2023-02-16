# Присвоение типа данных для вычислений
def check_data_type(x):
    if x.isnumeric() or x.replace("-","",1).isdigit():
        return int(x)
    elif x.count(".") == 1:
        return float(x)
    elif x.count(".") == 1 and x.replace("-", "").replace(".", "").isdigit():
        return float(x)

# Проверка данных, на текст и количество данных для сложения              
def check_data_user(x):
    b = []
    b.append(x[0])
    for i in range(1, len(x)):
        if sup(x[i]) == True:
            if x[i].replace('-','').replace('.','',1).isnumeric():
                b.append(x[i])
    if len(b) == len(x):
        if len(x) == 3 or len(x) == 5:
            return True

# Вспомогательный метод для проверки введенных данных
def sup(x):
    b = []
    for i in range(len(list(x))):
        if i == 0 and list(x)[i] == '-':
            b.append(list(x)[i])
        elif list(x)[i].isdigit():
            b.append(list(x)[i])
    if len(b) == len(list(x)):
        return True
         

# b = input()
# print(sup(b))
# print(list(b))
# b = ['/sum','1','2','3', '23-']
# print(check_data_user(b))
# print(check_data_user(input()))
# a = input()
# print(a.isdigit())