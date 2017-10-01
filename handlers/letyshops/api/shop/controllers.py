# -*-coding:utf-8;-*-
import json
import os
import urllib.parse

import requests

from handlers.letyshops.api.rountes import ROUTES

GET_TOP_SHOPS = ROUTES['get_top_shops']
GET_SHOP_INFO_BY_ID_ROUTE = ROUTES['get_shop_by_id']


# GET_ALL_SHOP_BY_CATEGORIES_ROUTE = ROUTES['get_shops_by_category']


def get_top_shops(token, country, limit=10, offset=0):
    url = urllib.parse.urljoin(os.getenv('API_URL'), GET_TOP_SHOPS).format(country, limit, offset)
    result = requests.get(url, headers={'Authorization': token}, verify=False)
    return json.loads(result.content.decode("utf-8"))['data']


def get_shop_by_id(token, *args, **kwargs):
    url = urllib.parse.urljoin(os.getenv('API_URL'), GET_SHOP_INFO_BY_ID_ROUTE).format(kwargs['shop_id'])
    result = requests.get(url, headers={'Authorization': token}, verify=False)
    return json.loads(result.content.decode("utf-8"))['data']


def render_shop_answer(bot, chat_id, shop_data_json):
    buttons = []
    buttons.append([InlineKeyboardButton('Перейти в магазин', url=shop_data_json['url'])])
    markup = InlineKeyboardMarkup(buttons, resize_keyboard=True)
    render_result = render_shop(shop_data_json)
    render_result = render_result.replace('&nbsp;', ' ', -1)
    return bot.send_message(chat_id=chat_id, text=render_result, parse_mode='Markdown',
                            reply_markup=markup)