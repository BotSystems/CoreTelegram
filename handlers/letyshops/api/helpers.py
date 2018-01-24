from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.letyshops.api.shop.inline_keyboards import shop_details_keyboard, shop_list_keyboard

class CallbackDataPositions:
    LIMIT = 3
    OFFSET = 5
    QUERY = 7

def attach_pager_buttons(buttons, pager, query, extra):
    limit, offset = pager.limit, pager.offset
    pagination_buttons = [[]]

    prev_callback_template = 'pager.prev.limit.{}.offset.{}.query.{}.{}'
    next_callback_template = 'pager.next.limit.{}.offset.{}.query.{}.{}'

    prev_callback = prev_callback_template.format(limit, offset, query, extra)
    next_callback = next_callback_template.format(limit, offset, query, extra)

    if pager.has_prev:
        pagination_buttons[0].append(InlineKeyboardButton('⬅', callback_data=prev_callback))

    if pager.has_next:
        pagination_buttons[0].append(InlineKeyboardButton('➡', callback_data=next_callback))

    return pagination_buttons + buttons + pagination_buttons

def to_keyboard(buttons):
    return InlineKeyboardMarkup(buttons)


def limit_offset_query(update):
    callback_data = update.callback_query.data.split('.')

    query = callback_data[CallbackDataPositions.QUERY]
    limit = callback_data[CallbackDataPositions.LIMIT]
    offset = callback_data[CallbackDataPositions.OFFSET]

    return (int(limit), int(offset), query)

def build_markup(keyboard, pager, query, *args, **kwargs):
    if pager:
        markup = attach_pager_buttons(keyboard, pager, query, kwargs.get('extra', '-'))
    markup = to_keyboard(markup)
    return markup

def edit_markup(bot, update, markup):

    callback_id = update.callback_query.id
    chat_id = update.callback_query.message.chat.id
    message_id = update.callback_query.message.message_id

    return bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, inline_message_id=None, reply_markup=markup)

def answer_with_edit(message, bot, update, markup, parse_mode=None):
    print(type(markup))
    # Если это CALLBACK - редактируем
    if update.callback_query:
        return edit_markup(bot, update, markup)
    return bot.send_message(update.message.chat.id, message, reply_markup=markup, parse_mode=parse_mode)
