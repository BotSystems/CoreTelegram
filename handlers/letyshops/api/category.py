# import json
# import os
# import urllib.parse
#
# import requests
# from telegram import InlineKeyboardMarkup, InlineKeyboardButton
# from telegram.ext import BaseFilter, ConversationHandler, MessageHandler, CallbackQueryHandler
#
# from handlers.decorators import save_chanel_decorator
# from handlers.letyshops.api.relogin.token_helpers import AUTH_TOKENS_STORAGE
# from handlers.letyshops.api.relogin.token_helpers import token_updater
# from handlers.letyshops.api.rountes import ROUTES
# from handlers.letyshops.api.shops import get_shop_by_category, get_shop_by_id, render_shop_answer
#
# GET_ALL_CATEGORIES_ROUTE = ROUTES['get_categories']
#
#
# @token_updater
# def get_categories(storage, *args, **kwarg):
#     url = urllib.parse.urljoin(os.getenv('API_URL'), GET_ALL_CATEGORIES_ROUTE)
#     access_token = storage['access_token']
#     return requests.get(url, headers={'Authorization': 'Bearer ' + access_token}, verify=False)
#
#
# CATEGORIES = get_categories(AUTH_TOKENS_STORAGE)
#
#
# def build_keyboard(category_list):
#     category_list = json.loads(category_list.content.decode("utf-8"))['data']
#     category_list = list(filter(lambda category: int(category['parent_id']), category_list))
#     category_list = sorted(category_list, key=lambda category: category['name'])
#     categories = []
#     for (category) in category_list:
#         category_keyboard = [InlineKeyboardButton(category['name'], callback_data='show_category.' + category['id'])]
#         categories.append(category_keyboard)
#     return categories
#
#
#
#
#
#
#
# category_handler = ConversationHandler(
#     entry_points=[MessageHandler(CategoryFilter(), show_all)],
#     states={
#         'CHOICE_CATEGORY': [CallbackQueryHandler(choice_category)],
#         'SHOW_SHOP': [CallbackQueryHandler(show_shop)],
#     },
#     fallbacks=[],
#     allow_reentry=True
# )
