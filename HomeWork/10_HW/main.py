import telebot
import config
import random

from telebot import types

i = 0

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def walcom(message):
    a = ['0',1,2,3,4,5,6,7,8,9]
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

    murkup.add(but1, but2, but3, but4, but5,but6,but7,but8,but9)
    bot.send_message(message.chat.id, 'Сделайте ход нажав на клавишу с номером поля', reply_markup=murkup)



bot.polling(none_stop=True)