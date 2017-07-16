#!/usr/bin/env python
import telegram
from flask import Flask, request
from telegram.ext import Updater
import os
from dotenv import load_dotenv
import os
from os.path import join, dirname
from telegram import Bot
from telegram.ext import Dispatcher
from handlers.handler import init_handlers

app = Flask(__name__)
bot = telegram.Bot(os.getenv('TOKEN'))
dispatcher = init_handlers(Dispatcher(bot, None, workers=0))

@app.route("/landing", methods=['GET', 'POST'])
def landing():
    return 'ok'

@app.route('/' + os.getenv('TOKEN'), methods=['GET', 'POST'])
def webhook_handler():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True))
        dispatcher.process_update(update)
        # chat_id = update.message.chat.id
        # text = update.message.text.encode('utf-8')
        # bot.sendMessage(chat_id=chat_id, text=text)
    return 'ok!'

if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    debug = os.getenv('DEBUG')

    app.run(host='0.0.0.0', port=port, debug=debug)



# def set_webhook(token, port, appname):
#     updater = Updater(token)
#     updater.bot.set_webhook("https://{}.herokuapp.com/".format(appname) + token)
#     updater.idle()
