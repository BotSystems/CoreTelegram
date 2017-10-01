import os

from handlers.decorators import save_chanel_decorator
from handlers.letyshops.api.category.builder import build_categories
from handlers.letyshops.api.category.controllers import get_categories
from handlers.letyshops.api.category.inline_keyboards import show_categories_keyboard
from handlers.letyshops.api.category.models import Category

TOKEN = '{} {}'.format(os.getenv('SERVER_TOKEN_PREFIX'), os.getenv('SERVER_TOKEN_VALUE'))


@save_chanel_decorator
def send_all_categories(bot, update, *args, **kwargs):
    try:
        category_json = get_categories(TOKEN)
        categories = build_categories(category_json)

        categories = Category.filter(categories)
        categories = Category.order(categories)
        markup = show_categories_keyboard(categories)

        return bot.send_message(chat_id=update.message.chat.id, text='Категории:', reply_markup=markup)
    except Exception as ex:
        print('Exception: ', ex)
