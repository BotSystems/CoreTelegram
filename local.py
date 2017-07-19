# -*- coding: utf-8 -*-
import os
from os.path import join, dirname

from dotenv import load_dotenv
from telegram.ext import Updater, ConversationHandler

from handlers.handler import init_handlers

dotenv_path = join(dirname(__file__), '.env.local')
load_dotenv(dotenv_path)

if __name__ == '__main__':
    token = os.getenv('TOKEN')
    updater = Updater(token=token)
    dispatcher = init_handlers(updater.dispatcher)
    updater.start_polling()
    updater.idle()
