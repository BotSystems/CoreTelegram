from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def shop_details_keyboard(shop_url):
    buttons = []
    buttons.append([InlineKeyboardButton('Перейти в магазин', url=shop_url)])
    return InlineKeyboardMarkup(buttons)


def shop_list_keyboard(shops):
    buttons = []
    for shop in shops:
        buttons.append([InlineKeyboardButton(shop.name.capitalize(), callback_data='show_shop_info.' + shop.id)])
    return InlineKeyboardMarkup(buttons)
