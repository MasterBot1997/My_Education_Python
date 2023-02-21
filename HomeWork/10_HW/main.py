import telebot
import config
from logg import *
from telebot import types
from Check_list import *

i = 1
a = ['0','1','2','3','4','5','6','7','8','9']
bot = telebot.TeleBot(config.TOKEN)

#Приветствие, и начало игры
@bot.message_handler(commands=['start'])
def walcom(message):
    global a
    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!\nЯ - {1.first_name} и это игра крестики нолики!'.format(message.from_user, bot.get_me()))
    bot.send_message(message.chat.id,f'Это наше игровое поле:\n'
                                                                f'| {a[1]} | {a[2]} | {a[3]} |\n'
                                                                '--------- \n'
                                                                f'| {a[4]} | {a[5]} | {a[6]} |\n'
                                                                '--------- \n'
                                                                f'| {a[7]} | {a[8]} | {a[9]} |\n')
    

    murkup = types.ReplyKeyboardMarkup(row_width=3)

    but1 = types.KeyboardButton('1')
    but2 = types.KeyboardButton('2')
    but3 = types.KeyboardButton('3')
    but4 = types.KeyboardButton('4')
    but5 = types.KeyboardButton('5')
    but6 = types.KeyboardButton('6')
    but7 = types.KeyboardButton('7')
    but8 = types.KeyboardButton('8')
    but9 = types.KeyboardButton('9')
    but10 = types.KeyboardButton('Начать сначала')

    murkup.add(but1, but2, but3, but4, but5,but6,but7,but8,but9,but10)
    bot.send_message(message.chat.id, 'Сделайте ход нажав на клавишу с номером поля', reply_markup=murkup)

@bot.message_handler(content_types=['text'])
def run_game(message):
    global a
    global i
    b = message.text
    if b.isnumeric():
        z = int(b)
    if check(message.text) == True:
        if message.text == 'Начать сначала':
            logger.debug(f'Игра наинается заново')
            i = 1
            a = ['0','1','2','3','4','5','6','7','8','9']
            bot.send_message(message.chat.id,'Игра начинается сначала')
        elif i % 2 == 0:
            for j in range(1,len(a)):
                if a[z] != 'X' and a[z] != 'O':
                    if b == a[j]:
                            logger.debug(f'Игрок 2 сходил на поле {z}')
                            i += 1 
                            a.pop(j)
                            a.insert(j, 'O')
                            bot.send_message(message.chat.id,'Сходил игрок 2')
                            break
                else:
                    logger.debug(f'Игрок 2 сходил на занятое поле {z}')
                    bot.send_message(message.chat.id,'Игрок 2, это поле занято. Сходите еще раз!')
                    break
        elif i % 2 != 0:
            i += 1
            for j in range(1,len(a)):
                if a[z] != 'X' and a[z] != 'O':
                    if b == a[j]:
                        logger.debug(f'Игрок 1 сходил на поле {z}')
                        a.pop(j)
                        a.insert(j, 'X')
                        bot.send_message(message.chat.id,'Сходил игрок 1')
                        break
                else:
                    logger.debug(f'Игрок 1 сходил на занятое поле {z}')
                    bot.send_message(message.chat.id,'Игрок 1, это поле занято. Сходите еще раз!')
                    break
        bot.send_message(message.chat.id,f'Игровое поле:\n'
                                            f'| {a[1]} | {a[2]} | {a[3]} |\n'
                                            '--------- \n'
                                            f'| {a[4]} | {a[5]} | {a[6]} |\n'
                                            '--------- \n'
                                            f'| {a[7]} | {a[8]} | {a[9]} |\n')
        if i >= 5:
            temp = check_win(a, i)
            if temp == 1:
                logger.debug('Выиграл игрок 1')
                bot.send_message(message.chat.id,'Выиграл игрок 1\n'
                                                'Следующие ходы уже будут новой игрой')
                i = 1
                a = ['0','1','2','3','4','5','6','7','8','9']
            elif temp == 2:
                logger.debug('Выиграл игрок 2')
                bot.send_message(message.chat.id,'Выиграл игрок 2\n'
                                                'Следкщие ходы уже будут новой игрой')
                i = 1
                a = ['0','1','2','3','4','5','6','7','8','9']
            elif temp == 3:
                logger.debug('Игра закончилась ничьей')
                bot.send_message(message.chat.id, 'Игра закончилась ничьей\n'
                                                    f'| {a[1]} | {a[2]} | {a[3]} |\n'
                                                    '--------- \n'
                                                    f'| {a[4]} | {a[5]} | {a[6]} |\n'
                                                    '--------- \n'
                                                    f'| {a[7]} | {a[8]} | {a[9]} |\n'
                                                    'Следующий ход будет новой игрой')
                i = 1
                a = ['0','1','2','3','4','5','6','7','8','9']
    else:
        bot.send_message(message.chat.id,'Такого варианта действия нет!\nПопробуйте еще раз.')
        logger.debug('Не верный ввод пользователем')


bot.polling(none_stop=True)