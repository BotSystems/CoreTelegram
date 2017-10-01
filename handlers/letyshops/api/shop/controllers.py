# -*-coding:utf-8;-*-
import json
import os
import urllib.parse

import requests

from handlers.letyshops.api.rountes import ROUTES

GET_TOP_SHOPS_ROUTE = ROUTES['get_top_shops']
GET_SHOP_INFO_BY_ID_ROUTE = ROUTES['get_shop_by_id']
GET_ALL_SHOP_BY_CATEGORIES_ROUTE = ROUTES['get_shops_by_category']
GET_SHOP_INFO_BY_NAME_ROUTE = ROUTES['get_shop_by_name']


def get_top_shops(token, country, limit=10, offset=0):
    url = urllib.parse.urljoin(os.getenv('API_URL'), GET_TOP_SHOPS_ROUTE).format(country, limit, offset)
    result = requests.get(url, headers={'Authorization': token}, verify=False)
    return json.loads(result.content.decode("utf-8"))['data']


def get_shop_by_id(token, *args, **kwargs):
    url = urllib.parse.urljoin(os.getenv('API_URL'), GET_SHOP_INFO_BY_ID_ROUTE).format(kwargs['shop_id'])
    result = requests.get(url, headers={'Authorization': token}, verify=False)
    return json.loads(result.content.decode("utf-8"))['data']


def get_shop_by_category(token, country, *args, **kwargs):
        url = urllib.parse.urljoin(os.getenv('API_URL'), GET_ALL_SHOP_BY_CATEGORIES_ROUTE).format(kwargs['category_id'], country)
        result = requests.get(url, headers={'Authorization': token}, verify=False)
        return json.loads(result.content.decode("utf-8"))['data']


def get_shop_by_name(token, *args, **kwargs):
    url = urllib.parse.urljoin(os.getenv('API_URL'), GET_SHOP_INFO_BY_NAME_ROUTE).format(kwargs['shop_name'])
    result = requests.get(url, headers={'Authorization': token}, verify=False)
    return json.loads(result.content.decode("utf-8"))['data']
