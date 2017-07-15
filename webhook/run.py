#!/usr/bin/env python
import telegram
from flask import Flask, request
from telegram.ext import Updater
import os
from app import app

# app = Flask(__name__)

global bot
bot = None

@app.route('/' + os.getenv('TOKEN', ''), methods=['GET', 'POST'])
def webhook_handler():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True))
        chat_id = update.message.chat.id
        text = update.message.text.encode('utf-8')
        bot.sendMessage(chat_id=chat_id, text=text)
    return 'ok'

def set_webhook(token, port, appname):
    updater = Updater(token)
    updater.bot.set_webhook("https://{}.herokuapp.com/".format(appname) + token)
    updater.idle()

def main(data_dict):
    token = data_dict['token']
    appname = data_dict['appname']
    port = data_dict['port']
    debug = data_dict['debug']
    # set_webhook(token, int(port), appname)
    bot = telegram.Bot(token=token)
    app.run(host='0.0.0.0', port=int(port), debug=debug)
