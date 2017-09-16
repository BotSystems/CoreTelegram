# -*- coding: utf-8 -*-
import json

from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, CommandHandler, Filters

from handlers.decorators import save_chanel_decorator
from handlers.letyshops.api.category import CategoryFilter
from handlers.letyshops.api.country import CountryFilter, country_handler
from handlers.letyshops.api.relogin.token_helpers import AUTH_TOKENS_STORAGE
from handlers.letyshops.api.shops import render_shop, find_shop_in_shops, get_shop_by_id, \
    top_shop_filter, try_to_get_shops_from_cache, TopShopsFilter


def build_keyboard():
    buttons = [[KeyboardButton('ТОП Магазинов')], [KeyboardButton('Категории')], [KeyboardButton('Указать страну')]]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def in_development_message(bot, update):
    message = 'In development...'
    bot.send_message(chat_id=update.message.chat.id, text=message)


@save_chanel_decorator
def send_shop_info(bot, update):
    shops = try_to_get_shops_from_cache(AUTH_TOKENS_STORAGE)

    bot.send_message(chat_id=update.message.chat.id, text='Запрос принят, ищу...')
    shop = find_shop_in_shops(str.strip(update.message.text), shops)
    if shop is None:
        return bot.send_message(chat_id=update.message.chat.id, text='Нет ничего такого :(')
    # подгружаем данные по ID
    shop_id = shop['id'] if isinstance(shop, dict) else None
    shop_full_response = get_shop_by_id(AUTH_TOKENS_STORAGE, shop_id=shop_id)
    if (shop_full_response.status_code == 200):
        shop_full_data = json.loads(shop_full_response.content.decode("utf-8"))['data']
        return bot.send_message(chat_id=update.message.chat.id, text=render_shop(shop_full_data), parse_mode='Markdown',
                                reply_markup=build_keyboard())
    # если поиск по ID вернул None, но имеется сокращенный объект магазина - рендерим его
    return bot.send_message(chat_id=update.message.chat.id, text=render_shop(shop), parse_mode='Markdown',
                            reply_markup=build_keyboard())


@save_chanel_decorator
def send_welcome(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Для получения информации о магазине - введите его название.",
                    reply_markup=build_keyboard())


@save_chanel_decorator
def send_top_shops(bot, update):
    shops_chunks = try_to_get_shops_from_cache(AUTH_TOKENS_STORAGE)
    top_shops = top_shop_filter(shops_chunks)

    top_shops = sorted(top_shops, key=lambda shop: shop['name'])
    prepare_for_render = []

    for shop in top_shops:
        prepare_for_render.append((shop['name'], shop['go_link']))

    buttons = []
    for (shop_name, shop_url) in prepare_for_render:
        buttons.append([InlineKeyboardButton(shop_name, url=shop_url)])
    markup = InlineKeyboardMarkup(buttons, resize_keyboard=True)
    return bot.send_message(chat_id=update.message.chat.id, text='ТОП Магазинов:', reply_markup=markup)


def init_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', send_welcome))
    dispatcher.add_handler(MessageHandler(TopShopsFilter(), send_top_shops))
    dispatcher.add_handler(MessageHandler(CategoryFilter(), in_development_message))
    dispatcher.add_handler(country_handler)
    dispatcher.add_handler(MessageHandler(Filters.text, send_shop_info))
    return dispatcher
