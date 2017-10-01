# -*-coding:utf-8;-*-
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from handlers.decorators import save_chanel_decorator
from handlers.letyshops.api.shop.builder import build_shops, build_shop
from handlers.letyshops.api.shop.controllers import get_top_shops, get_shop_by_id
from handlers.letyshops.api.shop.inline_keyboards import shop_details_keyboard

TOKEN = '{} {}'.format(os.getenv('SERVER_TOKEN_PREFIX'), os.getenv('SERVER_TOKEN_VALUE'))


@save_chanel_decorator
def send_top_shops(bot, update, *args, **kwargs):
    try:
        country = kwargs['country']
        top_shops_response = get_top_shops(TOKEN, country)
        shops = build_shops(top_shops_response)

        buttons = []
        for shop in shops:
            buttons.append([InlineKeyboardButton(shop.name.capitalize(), callback_data='show_shop_info.' + shop.id)])
        markup = InlineKeyboardMarkup(buttons)
        bot.send_message(chat_id=update.message.chat.id, text='ТОП 10 Магазинов:', reply_markup=markup)
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
        print(ex)
