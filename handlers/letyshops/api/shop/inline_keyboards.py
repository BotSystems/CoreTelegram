from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def shop_details_keyboard(shop_url):
    buttons = []
    buttons.append([InlineKeyboardButton('Перейти в магазин', url=shop_url)])
    return InlineKeyboardMarkup(buttons)
