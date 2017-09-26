# -*- coding: utf-8 -*-
import json

from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, CommandHandler, Filters, CallbackQueryHandler

from handlers.decorators import save_chanel_decorator
from handlers.letyshops.api.category import CategoryFilter, category_handler, choice_category, show_shop
from handlers.letyshops.api.country import CountryFilter, country_handler, save_country
from handlers.letyshops.api.relogin.token_helpers import AUTH_TOKENS_STORAGE
from handlers.letyshops.api.shops import render_shop, find_shop_in_shops, get_shop_by_id, \
    top_shop_filter, try_to_get_shops_from_cache, TopShopsFilter, render_shop_answer, get_top_shops, get_all_shops

from handlers.letyshops.api.country import show_all as country_show_all
from handlers.letyshops.api.category import show_all as category_show_all


def build_keyboard():
    buttons = [[KeyboardButton('ТОП 10 Магазинов')], [KeyboardButton('Категории')], [KeyboardButton('Указать страну')]]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def in_development_message(bot, update):
    message = 'In development...'
    bot.send_message(chat_id=update.message.chat.id, text=message)


@save_chanel_decorator
def find_shop_by_name(bot, update, *args, **kwargs):
    country = kwargs['country']
    bot.send_message(chat_id=update.message.chat.id, text='Запрос принят, ищу...')
    # shops = try_to_get_shops_from_cache(AUTH_TOKENS_STORAGE, country)
    shops = get_all_shops(AUTH_TOKENS_STORAGE, country)

    shop = find_shop_in_shops(str.strip(update.message.text), shops)
    if shop is None:
        return bot.send_message(chat_id=update.message.chat.id, text='Нет ничего такого :(')
    # подгружаем данные по ID
    shop_id = shop['id'] if isinstance(shop, dict) else None
    shop_full_response = get_shop_by_id(AUTH_TOKENS_STORAGE, shop_id=shop_id)
    if (shop_full_response.status_code == 200):
        shop_full_data_json = json.loads(shop_full_response.content.decode("utf-8"))['data']
        print(shop_full_data_json)
        render_shop_answer(bot, update.message.chat.id, shop_full_data_json)
    else:
        return bot.send_message(chat_id=update.message.chat.id, text='Нет ничего такого :(')


@save_chanel_decorator
def send_welcome(bot, update, *args, **kwargs):
    bot.sendMessage(chat_id=update.message.chat_id, text="Для получения информации о магазине - введите его название.",
                    reply_markup=build_keyboard())


# @save_chanel_decorator
# def send_top_shops(bot, update):
#     country = 'RU'
#     try:
#         shops_chunks = try_to_get_shops_from_cache(AUTH_TOKENS_STORAGE, country)
#         top_shops = top_shop_filter(shops_chunks)
#
#
#         print(top_shops)
#
#         top_shops = sorted(top_shops, key=lambda shop: shop['name'])
#         prepare_for_render = []
#
#         for shop in top_shops:
#             prepare_for_render.append((shop['name'], shop['id']))
#
#         buttons = []
#         for (shop_name, shop_id) in prepare_for_render[:10]:
#             # buttons.append([InlineKeyboardButton(shop_name, callback_data='show_shop_info.' + shop_id)])
#
#             print('show_shop_info.' + shop_id)
#             buttons.append([InlineKeyboardButton(shop_name, callback_data='show_shop_info.' + shop_id)])
#         markup = InlineKeyboardMarkup(buttons, resize_keyboard=True)
#         print(markup)
#         bot.send_message(chat_id=update.message.chat.id, text='ТОП 10 Магазинов:', reply_markup=markup)
#     except Exception as ex:
#         print(ex)

@save_chanel_decorator
def send_top_shops(bot, update, *args, **kwargs):
    limit = 10
    offset = 0
    country = kwargs['country']
    try:
        top_shops = get_top_shops(AUTH_TOKENS_STORAGE, country, limit, offset)

        prepare_for_render = []

        for shop in top_shops:
            prepare_for_render.append((shop['name'], shop['id']))

        buttons = []
        for (shop_name, shop_id) in prepare_for_render:
            buttons.append([InlineKeyboardButton(shop_name, callback_data='show_shop_info.' + shop_id)])
        markup = InlineKeyboardMarkup(buttons, resize_keyboard=True)
        bot.send_message(chat_id=update.message.chat.id, text='ТОП 10 Магазинов:', reply_markup=markup)
    except Exception as ex:
        print(ex)


def init_handlers(dispatcher):
    dispatcher.add_handler(MessageHandler(TopShopsFilter(), send_top_shops))

    dispatcher.add_handler(CommandHandler('start', send_welcome))

    dispatcher.add_handler(MessageHandler(CountryFilter(), country_show_all))
    dispatcher.add_handler(CallbackQueryHandler(save_country, False, False, 'set_country.*'))

    dispatcher.add_handler(MessageHandler(CategoryFilter(), category_show_all))
    dispatcher.add_handler(CallbackQueryHandler(choice_category, False, False, 'show_category.*'))
    dispatcher.add_handler(CallbackQueryHandler(show_shop, False, False, 'show_shop_info.*'))


    dispatcher.add_handler(MessageHandler(Filters.text, find_shop_by_name))

    return dispatcher
