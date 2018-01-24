import json
import os
import urllib.parse

import requests

from handlers.letyshops.api.rountes import ROUTES

GET_ALL_CATEGORIES_ROUTE = ROUTES['get_categories']


def get_categories(token, limit, offset):
    url = urllib.parse.urljoin(os.getenv('API_URL'), GET_ALL_CATEGORIES_ROUTE).format(limit, offset)
    print(url)
    result = requests.get(url, headers={'Authorization': token}, verify=False)
    result = json.loads(result.content.decode("utf-8"))
    return (result['data'], result['meta'])
    # return json.loads(result.content.decode("utf-8"))['data']

def get_selected_category(token, category_id):
    limit, offset = 100, 0
    categories, _ = get_categories(token, limit, offset)
    selected_category = list(filter(lambda c: c['id'] == category_id, categories))[0]
    return selected_category['name']
