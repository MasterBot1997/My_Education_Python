# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input("введите число: "))

my_list = [0, 1]
 
# for i in range (2, k + 1):
#     my_list.append(my_list[i-1] + my_list[i-2])
# for i in range (1, k + 1):
#     my_list.insert(0, ((-1)**(i+1))*my_list[i])

# print(my_list)

def fib (list, num):
    for i in range (1, num + 1):
        list.insert(0, ((-1)**(i+1)*list[i-1]))
    print(list)

fib(my_list, k)

