# -*- coding: utf-8 -*-
import json

from telegram.ext import MessageHandler, CommandHandler

from handlers.decorators import botan_decorator, save_chanel_decorator
from handlers.letyshops.api.relogin.token_helpers import AUTH_TOKENS_STORAGE
from handlers.letyshops.api.shops import render_shop, find_shop_in_shops, get_all_shops, get_shop_by_id


@botan_decorator('get_shop_info')
@save_chanel_decorator
def send_shop_info(bot, update):
    bot.send_message(chat_id=update.message.chat.id, text='Запрос принят, ищу...')
    shop = find_shop_in_shops(str.strip(update.message.text), get_all_shops(AUTH_TOKENS_STORAGE))
    if shop is None:
        return bot.send_message(chat_id=update.message.chat.id, text='Нет ничего такого :(')
    # подгружаем данные по ID
    shop_id = shop['id'] if isinstance(shop, dict) else None
    shop_full_response = get_shop_by_id(AUTH_TOKENS_STORAGE, shop_id=shop_id)
    if (shop_full_response.status_code == 200):
        shop_full_data = json.loads(shop_full_response.content.decode("utf-8"))['data']
        return bot.send_message(chat_id=update.message.chat.id, text=render_shop(shop_full_data), parse_mode='Markdown')
    # если поиск по ID вернул None, но имеется сокращенный объект магазина - рендерим его
    return bot.send_message(chat_id=update.message.chat.id, text=render_shop(shop), parse_mode='Markdown')


def send_welcome(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Для получения информации о магазине - введите его название.")


def init_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', send_welcome))
    dispatcher.add_handler(MessageHandler(None, send_shop_info))
    return dispatcher
