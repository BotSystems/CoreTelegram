# -*- coding: utf-8 -*-
from telegram.ext import MessageHandler
from models import Chanel


def save_chanel_decorator(fn):
    def wrapper(bot, update):
        print('SAVE CHANEL')
        Chanel.get_or_create(chanel_id=update.message.chat.id, defaults={'chanel_id': update.message.chat.id})
        return fn(bot, update)

    return wrapper


@save_chanel_decorator
def handler_echo(bot, update):
    print('HANDLER ECHO!')
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text.upper())


def init_handlers(dispatcher):
    dispatcher.add_handler(MessageHandler(None, handler_echo))
    return dispatcher
