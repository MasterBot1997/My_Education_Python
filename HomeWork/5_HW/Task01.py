# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

def new_list(count: int, alp = 'абв'):
    mid_list = []
    for i in range(count):
        a = sample(alp, k=3)
        mid_list.append("".join(a))
    return " ".join(mid_list)

def rep (word: str):
    return " ".join(i for i in word.split() if i != "абв")

lst = new_list(int(input()))
print(lst)
print(rep(lst))