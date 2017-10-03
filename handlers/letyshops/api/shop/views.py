# -*-coding:utf-8;-*-
import os

from handlers.decorators import save_chanel_decorator
from handlers.keyboard import build_keyboard
from handlers.letyshops.api.shop.builder import build_shops, build_shop
from handlers.letyshops.api.shop.controllers import get_top_shops, get_shop_by_id, get_shop_by_category, \
    get_shop_by_name
from handlers.letyshops.api.shop.inline_keyboards import shop_details_keyboard, shop_list_keyboard

TOKEN = '{} {}'.format(os.getenv('SERVER_TOKEN_PREFIX'), os.getenv('SERVER_TOKEN_VALUE'))


@save_chanel_decorator
def send_top_shops(bot, update, *args, **kwargs):
    try:
        country = kwargs['country']
        shops_json = get_top_shops(TOKEN, country)
        shops = build_shops(shops_json)

        markup = shop_list_keyboard(shops)
        return bot.send_message(update.message.chat.id, 'ТОП 10 Магазинов:', reply_markup=markup)
    except Exception as ex:
        print('Exception: ', ex)


@save_chanel_decorator
def send_shop_info(bot, update, *args, **kwargs):
    try:
        selected_shop_id = update.callback_query.data.split('.')[1]
        query = update.callback_query

        shop_json = get_shop_by_id(TOKEN, shop_id=selected_shop_id)
        shop = build_shop(shop_json)

        markup = shop_details_keyboard(shop.url)
        return bot.send_message(query.message.chat.id, shop.render(), parse_mode='Markdown', reply_markup=markup)
    except Exception as ex:
        print('Exception: ', ex)


@save_chanel_decorator
def send_shops_in_category(bot, update, *args, **kwargs):
    try:
        country = kwargs.get('country', 'ru')
        selected_category_id = update.callback_query.data.split('.')[1]
        query = update.callback_query

        shops_json = get_shop_by_category(TOKEN, country, category_id=selected_category_id)
        shops = build_shops(shops_json)

        markup = shop_list_keyboard(shops)
        return bot.send_message(query.message.chat.id, 'Магазины:', reply_markup=markup)
    except Exception as ex:
        print('Exception: ', ex)


@save_chanel_decorator
def find_shop_by_name(bot, update, *args, **kwargs):
    try:
        searching_shop_name = str.strip(update.message.text)
        bot.send_message(chat_id=update.message.chat.id, text='Запрос принят, ищу...', reply_markup=build_keyboard())

        shops_json = get_shop_by_name(TOKEN, shop_name=searching_shop_name)

        if (shops_json):
            first_shop_in_result = shops_json[0]

            shops_json = get_shop_by_id(TOKEN, shop_id=first_shop_in_result.get('id'))
            shop = build_shop(shops_json)

            markup = shop_details_keyboard(shop.url)
            return bot.send_message(update.message.chat.id, shop.render(), parse_mode='Markdown', reply_markup=markup)

        return bot.send_message(update.message.chat.id, 'Нет ничего такого :(')

    except Exception as ex:
        print('Exception: ', ex)
