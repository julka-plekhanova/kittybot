# # send_random_image.py

# from telegram import Bot
# import requests

# bot = Bot(token='5923379202:AAEFnlfMy3PMZlRwjujMR2rwWDHTTq5T4EM')
# URL = 'https://api.thecatapi.com/v1/images/search'
# chat_id = 69372143

# # Делаем GET-запрос к эндпоинту:
# response = requests.get(URL).json()
# # Извлекаем из ответа URL картинки:
# random_cat_url = response[0].get('url')  

# # Передаём chat_id и URL картинки в метод для отправки фото:
# bot.send_photo(chat_id, random_cat_url)

# kittybot/kittybot.py

# kittybot/kittybot.py

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from pprint import pprint
updater = Updater(token='5923379202:AAEFnlfMy3PMZlRwjujMR2rwWDHTTq5T4EM')

def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,text='Привет, я KittyBot!')

def wake_up(update, context):
    chat = update.effective_chat
    print(update.message )  # Отправим содержимое update в консоль
    context.bot.send_message(chat_id=chat.id, 
                             text='Спасибо, что включили меня')

updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling()
updater.idle()