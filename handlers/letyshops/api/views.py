from handlers.letyshops.api.shop.views import send_top_shops, send_shops_in_category
from handlers.letyshops.api.category.view import send_all_categories
from handlers.letyshops.api.helpers import limit_offset_query
from handlers.letyshops.api.constants import TOP_QUERY, CATEGORIES_QUERY, PAGER_STEP_SIZE, CATEGORY_QUERY

# ЭТИ ВСЕ Ф-И НАХОДЯТСЯ НА РАЗНЫХ УРОВНЯХ АБСТРАЦИЙ (ИСПРАВИТЬ ЭТУ ХУЙНЮ!)
def run_action_router(bot, update, limit, offset, query):
    if query == TOP_QUERY:
        send_top_shops(bot, update, limit=limit, offset=offset)
    elif query == CATEGORIES_QUERY:
        send_all_categories(bot, update, limit=limit, offset=offset)
    elif query == CATEGORY_QUERY:
        send_shops_in_category(bot, update, limit=limit, offset=offset)


def next_page(bot, update, *args, **kwargs):
    limit, offset, query = limit_offset_query(update)
    offset += PAGER_STEP_SIZE
    return run_action_router(bot, update, limit, offset, query)


def prev_page(bot, update, *args, **kwargs):
    limit, offset, query = limit_offset_query(update)
    offset -= PAGER_STEP_SIZE
    return run_action_router(bot, update, limit, offset, query)
