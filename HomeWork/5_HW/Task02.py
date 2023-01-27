# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

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

def rle_decoding (code_text="text_code_words.txt", decode_text="text_decode_words.txt"):
    if path.exists(code_text):
        with open(code_text) as my_f_1:
        # with open(code_text) as my_f_1, \
        #         open(decode_text, "a") as my_f_2:
            n = ""
            for k in my_f_1:
                w_num = []
                for i in k.strip():
                    if i.isdigit():
                        # Если написать n += 1 - тогда при декодировании
                        # будет плюсоваться 1(как строка) к кол-ву символов 
                        # начала след. строки и тогда декодинг не корректный 
                        n = i
                    else:
                        w_num.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x * y, w_num)))
                # my_f_2.write("".join(starmap(lambda x, y: x * y, w_num)))
                # Попробовал сделать запись сразу в файл, но в таком варианте
                # Все возвращается записью в одну строку
    else:
        print("Такого файла нет в системе!")


rle_encoding()
rle_decoding()
