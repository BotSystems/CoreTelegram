# -*- coding: utf-8 -*-

from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, Filters

from handlers.letyshops.api.category.filters import CategoryFilter
from handlers.letyshops.api.category.view import send_all_categories
from handlers.letyshops.api.country.filters import CountryFilter
from handlers.letyshops.api.country.views import send_countries, set_country
from handlers.letyshops.api.info.filters import WhatIsCashbackFilter, WantCashbackFilter
from handlers.letyshops.api.info.views import what_is_cashback, want_cashback
from handlers.letyshops.api.shop.filters import TopShopsFilter
from handlers.letyshops.api.shop.views import send_top_shops, send_shop_info, send_shops_in_category, find_shop_by_name
from handlers.letyshops.views import send_welcome


def init_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', send_welcome))
    dispatcher.add_handler(MessageHandler(TopShopsFilter(), send_top_shops))
    dispatcher.add_handler(CallbackQueryHandler(send_shop_info, False, False, 'show_shop_info.*'))
    dispatcher.add_handler(MessageHandler(CategoryFilter(), send_all_categories))
    dispatcher.add_handler(CallbackQueryHandler(send_shops_in_category, False, False, 'show_category.*'))
    dispatcher.add_handler(MessageHandler(CountryFilter(), send_countries))
    dispatcher.add_handler(CallbackQueryHandler(set_country, False, False, 'set_country.*'))
    dispatcher.add_handler(MessageHandler(WhatIsCashbackFilter(), what_is_cashback))
    dispatcher.add_handler(MessageHandler(WantCashbackFilter(), want_cashback))
    dispatcher.add_handler(MessageHandler(Filters.text, find_shop_by_name))
    return dispatcher
