from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from logg import *
from excep import *

# Приветственное меню если пользователь вошел первый раз и если вошел или запустил программу командой /start
# Так же если пользователь напишет hi выйдет данное приветствие
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_bro(update, context)
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!!!!\n'
                                     'Что бы перейти в меню нажми /menu')

# Это мое меню калькулятора с подсказками пользователю
async def menu_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_bro(update, context)
    await update.message.reply_text('Это мое небольшое меню пользователя нашего калькулятора:\n'
                                     '\nНаши маленькие правила пользования:\n'
                                     '- Ввод данных - нужно ввести 2 числа в однустроку с командой через пробел для рациональных чисел (Пример: /sum 1 1)\n'
                                     'и 4 числа для комплексных чисел (Пример: /sum 1 1 1 1)'
                                     '- При делении рациональных числ нельзя вводить второе значение 0 (Пример: /sum 1 0 - так записывать нельзя)\n'
                                     '- При делении комплексных чисел 3 и 4 значение одновременно не могут ровняться 0 (Пример: /sum 1 1 0 0 - такой записи быть не может)\n'
                                     '\nСписок команд:\n'
                                     '\n/sum - найти сумму рациональных или комплексных чисел\n'
                                     'sub - найти разницу рациональных или комплексных чисел\n'
                                     'mult - Умножение рациональных или комплексных чисел\n'
                                     'div - деление рациональных или комплексных чисел\n'
                                     'sqrt - возведение в степень рациональных или комплексных чисел/n'
                                     'Примечание:\n формат записи для возведения в степень:\n'
                                     '- для рациональных чисел первое число то что хотим возмести второе степень возведения(пример: /sqrt 1-число 2-степень)\n'
                                     '- для комплексных чисел первыее два числа составляющие, третье число степень(пример: /sqrt 1 2-числа 3-степень)\n')


async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bro(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    print(items)
    if check_data_user(items) == True:
        if len(items) == 3:
            x = check_data_type(items[1])
            y = check_data_type(items[2])
            await update.message.reply_text(f'{x} + {y} = {x+y}')
        else:
            x = complex(check_data_type(items[1]), check_data_type(items[2]))
            y = complex(check_data_type(items[3]), check_data_type(items[4]))
            c = complex(x+y)
            await update.message.reply_text(f'{x} + {y} = {c}')
    else:
        await update.message.reply_text(f'Данные введены не корректно.')

async def sub(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bro(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    if check_data_user(items) == True:
        if len(items) == 3:
            x = check_data_type(items[1])
            y = check_data_type(items[2])
            await update.message.reply_text(f'{x} - {y} = {x-y}')
        else:
            x = complex(check_data_type(items[1]), check_data_type(items[2]))
            y = complex(check_data_type(items[3]), check_data_type(items[4]))
            c = complex(x-y)
            await update.message.reply_text(f'{x} - {y} = {c}')
    else:
        await update.message.reply_text(f'Данные введены не корректно.')

async def mult(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bro(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    if check_data_user(items) == True:
        if len(items) == 3:
            x = check_data_type(items[1])
            y = check_data_type(items[2])
            await update.message.reply_text(f'{x} * {y} = {round(x*y, 4)}')
        else:
            x = complex(check_data_type(items[1]), check_data_type(items[2]))
            y = complex(check_data_type(items[3]), check_data_type(items[4]))
            c = complex(x*y)
            await update.message.reply_text(f'{x} * {y} = {c}')
    else:
        await update.message.reply_text(f'Данные введены не корректно.')

async def div(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bro(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    if check_data_user(items) == True:
        if len(items) == 3:
            x = check_data_type(items[1])
            # Проверка на 0 в знаменателе будет прямо тут
            if check_data_type(items[2]) != 0:
                y = check_data_type(items[2])
                await update.message.reply_text(f'{x} * {y} = {round(x/y, 4)}')
            else:
                await update.message.reply_text('Вы ввели 0 в знаменатель, попробуйте еще раз')
        else:
            x = complex(check_data_type(items[1]), check_data_type(items[2]))
            # Проверка на нули во второй пачке чисел для комплексных чисел
            if check_data_type(items[3]) != 0 or check_data_type(items[4]) != 0:
                y = complex(check_data_type(items[3]), check_data_type(items[4]))
                c = complex(x/y)
                await update.message.reply_text(f'{x} * {y} = {c}')
            else:
                await update.message.reply_text('Вы ввели оба значения второго комплексного числа равное 0. Попробуйте еще раз')
    else:
        await update.message.reply_text(f'Данные введены не корректно.')

async def sqrt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bro(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    if check_data_user(items) == True:
        if len(items) == 3:
            x = check_data_type(items[1])
            y = check_data_type(items[2])
            await update.message.reply_text(f'{x}^{y} = {round(x**y, 4)}')
    elif check_data_user_2(items):
        x = complex(check_data_type(items[1]), check_data_type(items[2]))
        y = check_data_type(items[3])
        c = x**y
        await update.message.reply_text(f'{x}^{y} = {c}')
    else:
        await update.message.reply_text(f'Данные введены не корректно.')

# async def help_bro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     log_bro(update, context)
#     await update.message.reply_text(f'/hi\n/time\n/help')

# async def time_bro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     log_bro(update, context)
#     await update.message.reply_text(f'{datetime.datetime.now().time()}')

# async def sum_bro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     log_bro(update, context)
#     msg = update.message.text
#     print(msg)
#     items = msg.split() #/sum 123 5678
#     x = complex(check_data_user(items[1]), check_data_user(items[2]))
#     y = complex(check_data_user(items[3]), check_data_user(items[4]))
#     c = complex(x+y)
#     await update.message.reply_text(f'{x} + {y} = {c}')



