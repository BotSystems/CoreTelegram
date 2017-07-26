# -*- coding: utf-8 -*-
from telegram.ext import MessageHandler, CommandHandler

from handlers.decorators import botan_decorator, save_chanel_decorator
from handlers.letyshops.api.relogin.token_helpers import AUTH_TOKENS_STORAGE
from handlers.letyshops.api.shops import render_shop, find_shop, get_all_shops


@botan_decorator('get_shop_info')
@save_chanel_decorator
def send_shop_info(bot, update):
    shop_name = str.strip(update.message.text)
    shop_data = render_shop(find_shop(shop_name, get_all_shops(AUTH_TOKENS_STORAGE)))
    if shop_data is None:
        return bot.send_message(chat_id=update.message.chat.id, text='Нет ничего такого :(')
    return bot.send_message(chat_id=update.message.chat.id, text=shop_data, parse_mode='Markdown')


def send_welcome(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Для получения информации о магазине - введите его название.")


def init_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', send_welcome))
    dispatcher.add_handler(MessageHandler(None, send_shop_info))
    return dispatcher
