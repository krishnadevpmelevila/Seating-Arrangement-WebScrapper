import os
from dotenv import load_dotenv
from telegram.ext import *
from scrap import scrap 
from telegram import Update, Bot
import requests
import re
# setup .env
load_dotenv()
token = os.environ.get("TOKEN")
bot = Bot(token)

# start command
def start(update:Update,context:CallbackContext):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Hello! I am the seat allotment bot. I will help you to get your seat allotment.")
    bot.send_message(chat_id=chat_id, text="Please type /seat to get your seat allotment.")

def seat(update:Update,context:CallbackContext):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Thankyou! Please wait for 6 seconds... I am getting it from the VJCET website....")
    link = scrap()
    bot.send_message(chat_id=chat_id, text="Almost here...")
    r = requests.get(link, allow_redirects=True)
    open('seat.pdf', 'wb').write(r.content)
    bot.send_message(chat_id=chat_id, text="Here it is! All the best for your exam!")
    bot.send_document(chat_id=chat_id, document=open('seat.pdf', 'rb'), filename="seat.pdf")

def main():
    updater = Updater(token,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('seat',seat))
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()