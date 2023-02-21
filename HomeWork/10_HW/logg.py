from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from loguru import logger

logger.add('log_info.log',
            format="{time} - {level} - {message}",
            level='DEBUG')