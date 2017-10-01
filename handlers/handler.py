# -*- coding: utf-8 -*-

from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler

from handlers.letyshops.api.shop.filters import TopShopsFilter
from handlers.letyshops.api.shop.views import send_top_shops, send_shop_info
from handlers.letyshops.views import send_welcome


def init_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', send_welcome))
    dispatcher.add_handler(MessageHandler(TopShopsFilter(), send_top_shops))
    dispatcher.add_handler(CallbackQueryHandler(send_shop_info, False, False, 'show_shop_info.*'))
    # dispatcher.add_handler(MessageHandler(WhatIsCashbackFilter(), what_is_cashback))
    # dispatcher.add_handler(MessageHandler(WantCashbackFilter(), want_cashback))
    # dispatcher.add_handler(MessageHandler(CountryFilter(), country_show_all))
    # dispatcher.add_handler(CallbackQueryHandler(save_country, False, False, 'set_country.*'))
    # dispatcher.add_handler(MessageHandler(CategoryFilter(), category_show_all))
    # dispatcher.add_handler(CallbackQueryHandler(choice_category, False, False, 'show_category.*'))
    # dispatcher.add_handler(MessageHandler(Filters.text, find_shop_by_name))
    return dispatcher
