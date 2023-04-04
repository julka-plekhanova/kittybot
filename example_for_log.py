# example_for_log.py
import os

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from dotenv import load_dotenv 

load_dotenv()
secret_token = os.getenv('TOKEN')
updater = Updater(token=secret_token)

def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,text='Привет, я KittyBot!')

def wake_up(update, context):
    chat = update.effective_chat
    print(update)  # Отправим содержимое update в консоль
    print(context)
    context.bot.send_message(chat_id=chat.id, 
                             text='Спасибо, что включили меня')

updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling()
updater.idle()