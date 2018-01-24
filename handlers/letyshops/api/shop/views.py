# -*-coding:utf-8;-*-
import os

from handlers.decorators import save_chanel_decorator
from handlers.keyboard import build_keyboard
from handlers.letyshops.api.shop.builder import build_shops, build_shop
from handlers.letyshops.api.shop.controllers import get_top_shops, get_shop_by_id, get_shop_by_category, \
    get_shop_by_name
from handlers.letyshops.api.shop.inline_keyboards import shop_details_keyboard, shop_list_keyboard
from handlers.paging.page import Page
from handlers.letyshops.api.category.view import send_all_categories
from handlers.letyshops.api.helpers import build_markup, answer_with_edit, limit_offset_query
from handlers.letyshops.api.constants import TOP_QUERY, TOKEN, CATEGORY_QUERY
from handlers.letyshops.api.category.controllers import get_selected_category

@save_chanel_decorator
def send_top_shops(bot, update, *args, **kwargs):
    limit, offset = kwargs.get('limit', 5), kwargs.get('offset', 0)
    try:
        country = kwargs['country']
        shops, meta = get_top_shops(TOKEN, country, limit, offset)
        shops = build_shops(shops)

        markup = build_markup(shop_list_keyboard(shops), Page(meta), TOP_QUERY)
        return answer_with_edit('*ТОП Магазинов:*', bot, update, markup, 'Markdown')
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
        print('Exception: ', ex)


@save_chanel_decorator
def send_shops_in_category(bot, update, *args, **kwargs):
    limit, offset = kwargs.get('limit', 5), kwargs.get('offset', 0)
    try:
        country = kwargs.get('country', 'ru')

        callback_query_array = update.callback_query.data.split('.')
        if (len(callback_query_array)) > 7:
            selected_category_id = update.callback_query.data.split('.')[8]
        else:
            selected_category_id = update.callback_query.data.split('.')[1]

        selected_category_title = get_selected_category(TOKEN, selected_category_id)
        
        query = update.callback_query

        shops, meta = get_shop_by_category(TOKEN, country, selected_category_id, limit, offset)
        shops = build_shops(shops)

        markup = build_markup(shop_list_keyboard(shops), Page(meta), CATEGORY_QUERY, extra=selected_category_id)
        
        if (len(callback_query_array)) > 7:
            chat_id = update.callback_query.message.chat.id
            message_id = update.callback_query.message.message_id
            return bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, inline_message_id=None, reply_markup=markup)
        else:
            return bot.send_message(query.message.chat.id, '*Магазины (*{}*):*'.format(selected_category_title), reply_markup=markup, parse_mode = 'Markdown')
    except Exception as ex:
        print('Exception: ', ex)


@save_chanel_decorator
def find_shop_by_name(bot, update, *args, **kwargs):
    try:
        searching_shop_name = str.strip(update.message.text)
        bot.send_message(chat_id=update.message.chat.id, text='Запрос принят, ищу...', reply_markup=build_keyboard())

        shops_json = get_shop_by_name(TOKEN, shop_name=searching_shop_name)

        if (shops_json):
            first_shop_in_result = shops_json[0]

            shops_json = get_shop_by_id(TOKEN, shop_id=first_shop_in_result.get('id'))
            shop = build_shop(shops_json)

            markup = shop_details_keyboard(shop.url)
            return bot.send_message(update.message.chat.id, shop.render(), parse_mode='Markdown', reply_markup=markup)

        return bot.send_message(update.message.chat.id, 'Нет ничего такого :(')

    except Exception as ex:
        print('Exception: ', ex)
