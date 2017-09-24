# -*- coding: utf-8 -*-
from models import Chanel


def save_chanel_decorator(fn):
    def wrapper(bot, update, *args, **kwargs):

        if (update.callback_query):
            chat_id = update.callback_query.message.chat.id
        else:
            chat_id = update.message.chat.id

        cid, _ = Chanel.get_or_create(chanel_id=chat_id, defaults={'chanel_id': chat_id})
        return fn(bot, update, country=cid.country)

    return wrapper
