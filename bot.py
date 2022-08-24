import os
from dotenv import load_dotenv
from telegram.ext import *
from scrap import scrap
from telegram import Update, Bot
import requests
import re
import http.server
import socketserver
import time

# setup .env
load_dotenv()
token = os.environ.get("TOKEN")
bot = Bot(token)


# start command
def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    bot.send_message(
        chat_id=chat_id, text="Hello! I am the seat allotment bot. I will help you to get your seat allotment.")
    bot.send_message(
        chat_id=chat_id, text="Please type /seat to get your seat allotment.")
def author(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="This bot is developed by Krishnadev P Melevila, CSEA 2021-2025 VJCET\nInsta:https://instagram.com/krishnadev_p_melevila\nWebsite:https://krishnadevpmelevila.com\nIf there any bug in this bot please report to +918089188971 on Whatsapp! Thnx in advance:)")

def seat(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    bot.send_message(
        chat_id=chat_id, text="Thankyou! Please wait for 6 seconds... I am getting it from the VJCET website....")
    os.remove("seat.pdf")
    link = scrap()
   

    bot.send_message(chat_id=chat_id, text="Almost here...")
    r = requests.get(link, allow_redirects=True)
    open('seat.pdf', 'wb').write(r.content)
    bot.send_message(
        chat_id=chat_id, text="Here it is! All the best for your exam!")
    bot.send_document(chat_id=chat_id, document=open(
        'seat.pdf', 'rb'), filename="seat.pdf")

updater = Updater(token, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler('seat', seat))
dp.add_handler(CommandHandler('author', author))
dp.add_handler(CommandHandler('start', start))
updater.start_polling()


# start http server on port 3000
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 3000
my_server = socketserver.TCPServer(("", PORT), handler_object)
print("Server started!")
# Star the server
my_server.serve_forever()
