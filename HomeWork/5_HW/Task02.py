# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# from itertools import groupby, starmap
# from os import path


# def rle_encoding (text="text_words.txt", code_text="text_code_words.txt"):
#     if path.exists(text):
#         with open(text) as my_f_1, \
#                 open(code_text, "a") as my_f_2:
#             for i in my_f_1:
#                 my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
#     else:
#         print("Такого файла нет в системе!")

# rle_encoding()

from itertools import groupby, starmap
from os import path


def rle_encoding (text="text_words.txt", code_text="text_code_words.txt"):
    if path.exists(text):
        with open(text) as my_f_1, \
                open(code_text, "a") as my_f_2:
            for i in my_f_1:
                my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("Такого файла нет в системе!")

# def rle_decoding (name):
#     if path.exists(name):
#         with open(name) as my_f_1:
#             n = ""
#             for k in my_f_1:
#                 w_num = []
#                 for i in k.strip():
#                     if i.isdigit():
#                         n += i
#                     else:
#                         w_num.append([int(n), i])
#                         n = ""
#                 print("".join(starmap(lambda x, y: x * y, w_num)))
#     else:
#         print("Такого файла нет в системе!")


rle_encoding()
# rle_decoding("text_decode_words.txt")
