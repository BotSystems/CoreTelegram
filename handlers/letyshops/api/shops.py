# -*-coding:utf-8;-*-
import json
import os
import urllib.parse

import requests

from handlers.letyshops.api.relogin.token_helpers import token_updater

SHOPS_ROUTE = 'shops?page[offset]={}&page[limit]={}'


@token_updater
def get_shops(storage, limit, offset):
    url = urllib.parse.urljoin(os.getenv('API_URL'), SHOPS_ROUTE).format(offset, limit)
    access_token = storage['access_token']
    return requests.get(url, headers={'Authorization': 'Bearer ' + access_token}, verify=False)


def get_all_shops(storage):
    limit, offset = 100, 0
    while True:
        result = json.loads(get_shops(storage, limit, offset).content.decode("utf-8"))['data']
        if result:
            offset = offset + limit
            yield result
        else:
            break


def render_shop(shop):
    if shop is None:
        return None

    name = shop['name']
    logo = shop['image']
    url = shop['go_link']

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

    template = '[{}]({})\nКэшбэк: {} {}{}\n[Перейти в магазин]({})'
    data = [name, logo, cashback_type_floated, cashback_rate_value, cashback_rate_type, url]

    if all([(cashback_setting is None) for cashback_setting in [cashback_rate_value, cashback_rate_type, cashback_type_floated]]):
        template = '[{}]({})\n[Перейти в магазин]({})'
        data = [name, logo, url]

    return template.format(*data)


def find_shop(searching_shop, shop_list):
    shops = (item for it in shop_list for item in it)
    for shop in shops:
        if searching_shop.lower() in [shop_alias.lower() for shop_alias in  shop['aliases']]:
            return shop
