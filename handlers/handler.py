# -*- coding: utf-8 -*-
from telegram.ext import Updater, MessageHandler
import os


def handler_echo(bot, update):
    print('HANDLER ECHO!')
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text.upper())

def init_handlers(dispatcher):
    dispatcher.add_handler(MessageHandler(None, handler_echo))
    return dispatcher
