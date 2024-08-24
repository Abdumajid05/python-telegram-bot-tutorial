import os
import telegram
from telegram.ext import CommandHandler, Updater,MessageHandler
from telegram import Update

TOKEN = os.environ['TOKEN']


def echo(update: Update, context):
    return(update['message']['text'])

def send_message(update: Update, context):
    pass

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(filters=None, callback=echo))

updater.start_polling()
updater.idle()
