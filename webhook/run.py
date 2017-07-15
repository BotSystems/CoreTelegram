#!/usr/bin/env python

import telegram
from flask import Flask, request
from telegram.ext import Updater

app = Flask(__name__)

global bot
global data_dict

bot = None
data_dict = None

@app.route('/hook', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True))

        chat_id = update.message.chat.id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')

        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=text)

    return 'ok'

def set_webhook(token, port, appname):
    updater = Updater(token)
    # add handlers
    updater.start_webhook(listen="0.0.0.0", port=port, url_path=token)
    updater.bot.set_webhook("https://{}.herokuapp.com/hook/".format(appname) + token)
    updater.idle()

@app.route('/')
def index():
    return '.'

def main(data_dict):
    token = data_dict['token']
    appname = data_dict['appname']
    port = data_dict['port']
    debug = data_dict['debug']

    # print(type(port))

    set_webhook(token, int(port), appname)
    bot = telegram.Bot(token=token)
    app.run(host='0.0.0.0', port=port, debug=debug)
