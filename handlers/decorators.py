# -*- coding: utf-8 -*-
from models import Chanel


def save_chanel_decorator(fn):
    def wrapper(bot, update):
        Chanel.get_or_create(chanel_id=update.message.chat.id, defaults={'chanel_id': update.message.chat.id})
        return fn(bot, update)

    return wrapper
