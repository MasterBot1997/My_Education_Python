from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from logg import *

async def hi_bro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bro(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

async def help_bro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bro(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help')

async def time_bro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bro(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_bro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_bro(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() #/sum 123 5678
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')