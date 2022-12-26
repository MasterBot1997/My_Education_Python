# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

n = []
k = int(input("Enter the value of N: "))
for i in range (-k, k + 1):
    n.append(i)
print (n)

pos_one = int(input("Position one: "))
pos_two = int(input("Position two: "))
if pos_one < 0 or pos_two < 0 or pos_one > k * 2 + 1 or pos_two > k * 2 + 1:
    print('There are no values for these indexes!')
else:
    z = n[pos_one - 1] * n[pos_two - 1]
    print(z)