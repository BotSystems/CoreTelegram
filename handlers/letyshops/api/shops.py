# -*-coding:utf-8;-*-
import json
import os
import urllib.parse

import requests
import re

from requests import Response
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import BaseFilter

from handlers.decorators import save_chanel_decorator
from handlers.letyshops.api.relogin.token_helpers import token_updater
from handlers.letyshops.api.rountes import ROUTES



GET_ALL_SHOPS_ROUTE = ROUTES['get_shops']
GET_SHOP_INFO_BY_ID_ROUTE = ROUTES['get_shop_by_id']
GET_ALL_SHOP_BY_CATEGORIES_ROUTE = ROUTES['get_shops_by_category']

mini_cache = []


def render_shop(shop):
    if shop is None:
        return None

    name = shop['name']
    logo = shop['image']
    # url = shop['url']
    cashback_waiting_days = shop['cashback_waiting_days'] if shop.get('cashback_waiting_days') else 'Не указано'
    description = shop['description'] if shop['description'] is not None else 'Отсутствует'

    cashback_rate_value = None
    cashback_rate_type = None
    cashback_type_floated = None

    if isinstance(shop['cashback_rate'], dict):
        cashback_rate_value = shop['cashback_rate']['value'] if 'value' in shop['cashback_rate'] else None
        cashback_rate_type = shop['cashback_rate']['rate_type'] if 'rate_type' in shop['cashback_rate'] else None
        cashback_type_floated = shop['cashback_rate']['is_floated'] if 'is_floated' in shop['cashback_rate'] else None

    if cashback_rate_type is not None:
        cashback_rate_type = '%' if cashback_rate_type == 'percent' else cashback_rate_type

    if cashback_type_floated is not None:
        cashback_type_floated = 'до' if cashback_type_floated is True else ''

    template = '[{}]({})\n*Кэшбэк:* {} {}{}\n*Доп. инфо:* {}\n*Длительность ожидания кэшбэка:* {}'
    description = re.sub(r'<[^>]*?>', '', description)
    description = re.sub(r'[*]', '', description)
    description = re.sub(r'&nbsp;', ' ', description)
    data = [name, logo, cashback_type_floated, cashback_rate_value, cashback_rate_type, description.strip(), cashback_waiting_days]
    # data = [name, logo, cashback_type_floated, cashback_rate_value, cashback_rate_type, '', cashback_waiting_days]
    print(description)

    if all([(cashback_setting is None) for cashback_setting in
            [cashback_rate_value, cashback_rate_type, cashback_type_floated]]):
        template = '[{}]({})\n*Доп. инфо:* {}\n*Длительность ожидания кэшбэка:* {}'
        data = [name, logo, re.sub(r'<[^>]*?>', '', description), cashback_waiting_days]

    return template.format(*data)


@token_updater
def get_shop_by_id(storage, *args, **kwargs) -> Response:
    if (kwargs.get('shop_id')):
        url = urllib.parse.urljoin(os.getenv('API_URL'), GET_SHOP_INFO_BY_ID_ROUTE).format(kwargs['shop_id'])
        access_token = storage['access_token']
        return requests.get(url, headers={'Authorization': 'Bearer ' + access_token}, verify=False)
    return None

@token_updater
def get_shop_by_category(storage, country, *args, **kwargs) -> Response:
    print(kwargs)
    # country = kwargs['chanel'].country
    if (kwargs.get('category_id')):
        url = urllib.parse.urljoin(os.getenv('API_URL'), GET_ALL_SHOP_BY_CATEGORIES_ROUTE).format(kwargs['category_id'], country)
        print(url)
        access_token = storage['access_token']
        return requests.get(url, headers={'Authorization': 'Bearer ' + access_token}, verify=False)
    return None


def get_all_shops(storage, country):
    print('upload shops')

    @token_updater
    def get_shops(storage, *args, **kwargs):
        limit, offset = kwargs['limit'], kwargs['offset']
        url = urllib.parse.urljoin(os.getenv('API_URL'), GET_ALL_SHOPS_ROUTE).format(country, offset, limit)
        print(url)
        access_token = storage['access_token']
        return requests.get(url, headers={'Authorization': 'Bearer ' + access_token}, verify=False)

    limit, offset = 100, 0
    while True:
        result = json.loads(get_shops(storage, limit=limit, offset=offset).content.decode("utf-8"))['data']
        if result:
            offset = offset + limit
            yield result
        else:
            break


def find_shop_in_shops(searching_shop, shop_list):
    shops = (item for it in shop_list for item in it)
    for shop in shops:
        shop['aliases'].append(shop['name'].lower())
        if searching_shop.lower() in [shop_alias.lower() for shop_alias in shop['aliases']]:
            return shop


def top_shop_filter(shop_chunks):
    result = []

    for chunk in shop_chunks:
        top_shops_in_chunk = list(filter(lambda shop: shop['top'], chunk))
        for shop in top_shops_in_chunk:
            result.append(shop)
    return result


def top_shops(shop_list):
    print('TOP SHOPS')


def try_to_get_shops_from_cache(storage, country):
    if mini_cache:
        return mini_cache

    shops = get_all_shops(storage, country)
    for shop in shops:
        mini_cache.append(shop)

    return try_to_get_shops_from_cache(storage, country)


class TopShopsFilter(BaseFilter):
    def filter(self, message):
        return 'ТОП 10 Магазинов' in message.text


def render_shop_answer(bot, chat_id, shop_data_json):
    buttons = []
    buttons.append([InlineKeyboardButton('Перейти в магазин', url=shop_data_json['url'])])
    markup = InlineKeyboardMarkup(buttons, resize_keyboard=True)
    render_result = render_shop(shop_data_json)
    render_result = render_result.replace('&nbsp;', ' ', -1)
    return bot.send_message(chat_id=chat_id, text=render_result, parse_mode='Markdown',
                            reply_markup=markup)


def get_top_shops(storage, country, limit, offset):
    url = urllib.parse.urljoin(os.getenv('API_URL'), GET_ALL_SHOPS_ROUTE).format(country, offset, limit)
    access_token = storage['access_token']
    result = requests.get(url, headers={'Authorization': 'Bearer ' + access_token}, verify=False)
    return json.loads(result.content.decode("utf-8"))['data']
