# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import groupby, starmap
from os import path


def rle_encoding(text="text_words.txt", code_text="text_code_words.txt"):
    if path.exists(text):
        with open(text, "r") as my_f_1, \
                open(code_text, "w") as my_f_2:
            for i in my_f_1:
                my_f_2.write(
                    "".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("Такого файла нет в системе!")

# Вариант с (n = 1) вместо (n += i), в данном варианте происходит корректный вывод в консоль
# def rle_decoding (code_text="text_code_words.txt", decode_text="text_decode_words.txt"):
#     if path.exists(code_text):
#         with open(code_text) as my_f_1:
#             n = ""
#             for k in my_f_1:
#                 w_num = []
#                 for i in k.strip():
#                     if i.isdigit():
#                         n = i
#                     else:
#                         w_num.append([int(n), i])
#                         n = ""
#                 print("".join(starmap(lambda x, y: x * y, w_num)))
#     else:
#         print("Такого файла нет в системе!")

# ------------------------------------------------------------------------------------------------------------------

# Вариант с (n += i), в эом варианте вывод в консоль будет не корректным(текст будет выводиться с неверным количеством символов)
# Например: превая строка 2а2А1\n вторая 2с2С, "1" которая в кнце строки приплюсуется строчно к следующей и получится 12с вместо 2с.

# def rle_decoding(code_text="text_code_words.txt", decode_text="text_decode_words.txt"):
#     if path.exists(code_text):
#         with open(code_text) as my_f_1:
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

# -------------------------------------------------------------------------------------------------------------

# Варинат с записью декодированного текста в файл(записывает только в одну строку все, так и не удалось сделать корректным)
def rle_decoding(code_text="text_code_words.txt", decode_text="text_decode_words.txt"):
    if path.exists(code_text):
        with open(code_text, "r") as my_f_1, \
                open(decode_text, "w") as my_f_2:
            n = ""
            for k in my_f_1:
                w_num = []
                for i in k.strip():
                    if i.isdigit():
                        n = i
                    else:
                        w_num.append([int(n), i])
                        n = ""
            my_f_2.writelines("".join(starmap(lambda x, y: x * y, w_num)))
            print("".join(starmap(lambda x, y: x * y, w_num)))
    else:
        print("Такого файла нет в системе!")


rle_encoding()
rle_decoding()
