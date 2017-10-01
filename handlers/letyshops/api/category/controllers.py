import json
import os
import urllib.parse

import requests

from handlers.letyshops.api.rountes import ROUTES

GET_ALL_CATEGORIES_ROUTE = ROUTES['get_categories']


def get_categories(token, *args, **kwarg):
    url = urllib.parse.urljoin(os.getenv('API_URL'), GET_ALL_CATEGORIES_ROUTE)
    result = requests.get(url, headers={'Authorization': token}, verify=False)
    return json.loads(result.content.decode("utf-8"))['data']
