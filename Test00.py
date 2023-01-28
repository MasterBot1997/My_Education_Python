from itertools import groupby, starmap
from os import path

def rle_encoding(text="text_words.txt", code_text="encode.txt"):
    if path.exists(text):
        with open(text, "r") as my_f_1, \
                open(code_text, "a") as my_f_2:
            for i in my_f_1:
                my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("Такого файла нет в системе!")

# def rle_decoding(code_text="text_code_words.txt", decode_text="text_decode_words.txt"):
#     if path.exists(code_text):
#         # with open(code_text) as my_f_1:
#         with open(code_text) as my_f_1, \
#                 open(decode_text, "a") as my_f_2:
#             n = ""
#             for k in my_f_1:
#                 w_num = []
#                 for i in k.strip():
#                     if i.isdigit():
#                         # Если написать n += 1 - тогда при декодировании
#                         # будет плюсоваться 1(как строка) к кол-ву символов
#                         # начала след. строки и тогда декодинг не корректный
#                         n = i
#                     else:
#                         w_num.append([int(n), i])
#                         n = ""
#                     my_f_2.writelines("".join(starmap(lambda x, y: x * y, w_num)))
#                 print("".join(starmap(lambda x, y: x * y, w_num)))
#                         # Попробовал сделать запись сразу в файл, но в таком варианте
#                         # Все возвращается записью в одну строку
#         print("Такого файла нет в системе!")

# def rle_decoding():
#     with open("encode.txt", "r") as my_f_1, \
#                 open("decode.txt", "w") as my_f_2:
#             n = ''
#             for line in my_f_1:
#                 i = 0
#                 while i in range(len(line)):
#                     if line[i] == '-': 
#                         i+=1
#                         n = n + line[i+1:i+1+int(line[i])]
#                         i = i+int(line[i])+1
#                     elif int(line[i]) > 1:
#                         n = n + line[i+1]*int(line[i])
#                         i+=2
#                 print (n)
#             my_f_2.write(n)

# rle_encoding()
# rle_decoding()

with open("encode.txt", "r") as in_file:
    with open("decode.txt", "w") as out_file:
        result = ''
        for line in in_file:
            i = 0
            while i in range(len(line) - 2):


                if line[i] == 1: 
                    i+=1
                    result = result + line[i+1:i+1+int(line[i])]
                    i = i+int(line[i])+1
                
                elif int(line[i]) > 1:
                    result = result + line[i+1]*int(line[i])
                    i+=2

            print (result)
        out_file.write(result)