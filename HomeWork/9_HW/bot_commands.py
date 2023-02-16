from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from logg import *
from excep import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_bro(update, context)
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!!!!\n'
                                     'Что бы перейти в меню нажми /menu')
async def menu_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_bro(update, context)
    await update.message.reply_text('Это мое небольшое меню пользователя нашего калькулятора:\n'
                                     '\n/sum - найти сумму рациональных или комплексных чисел, нужно ввести 1 и 2 число в однустроку с командой через пробел\n(Пример: /sum 1 1)')

async def sum_bro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bro(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
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



