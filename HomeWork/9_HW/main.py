from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5675216545:AAFeITy9wvOumeG-Yntz5jnnnhmuvocOAJQ").build()

app.add_handler(CommandHandler("hi", hi_bro))
app.add_handler(CommandHandler("time", time_bro))
app.add_handler(CommandHandler("help", help_bro))
app.add_handler(CommandHandler("sum", sum_bro))

print('server start')
app.run_polling()