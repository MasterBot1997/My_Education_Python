from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

def log_bro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('ds.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}''\n')
    file.close()