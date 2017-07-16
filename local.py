# -*- coding: utf-8 -*-
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
from dotenv import load_dotenv
import os
from os.path import join, dirname
from handlers.handler import init_handlers
from telegram.ext import Updater


dotenv_path = join(dirname(__file__), '.env.bleat')
load_dotenv(dotenv_path)


if __name__ == '__main__':
    token = os.getenv('TOKEN')
    updater = Updater(token=token)
    dispatcher = init_handlers(updater.dispatcher)
    updater.start_polling()
    updater.idle()
