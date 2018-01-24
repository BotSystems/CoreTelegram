import os

from handlers.decorators import save_chanel_decorator
from handlers.letyshops.api.category.builder import build_categories
from handlers.letyshops.api.category.controllers import get_categories
from handlers.letyshops.api.category.inline_keyboards import show_categories_keyboard
from handlers.letyshops.api.category.models import Category
from handlers.paging.page import Page
from handlers.letyshops.api.helpers import build_markup, answer_with_edit
from handlers.letyshops.api.constants import CATEGORIES_QUERY, TOKEN

@save_chanel_decorator
def send_all_categories(bot, update, *args, **kwargs):
    limit, offset = kwargs.get('limit', 5), kwargs.get('offset', 0)
    try:
        categories_data, meta = get_categories(TOKEN, limit, offset)
        categories = build_categories(categories_data)

        # Убрать из списка подкатегории?
        # categories = Category.filter(categories)
        categories = Category.order(categories)

        markup = build_markup(show_categories_keyboard(categories), Page(meta), CATEGORIES_QUERY)
        return answer_with_edit('*Категории:*', bot, update, markup, 'Markdown')
    except Exception as ex:
        print('Exception: ', ex)
