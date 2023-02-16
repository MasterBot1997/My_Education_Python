from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5675216545:AAFeITy9wvOumeG-Yntz5jnnnhmuvocOAJQ").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("Hi", start))
app.add_handler(CommandHandler("menu", menu_user))
app.add_handler(CommandHandler("sum", sum))
app.add_handler(CommandHandler("sub", sub))
app.add_handler(CommandHandler("mult", mult))
app.add_handler(CommandHandler("div", div))
app.add_handler(CommandHandler("sqrt", sqrt))

print('server start')
app.run_polling()



# app.add_handler(CommandHandler("help", help_bro))