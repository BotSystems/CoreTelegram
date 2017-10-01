from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def show_categories_keyboard(categories):
    result = []
    for category in categories:
        print(category.title)
        result.append([InlineKeyboardButton(category.title, callback_data='show_category.' + category.id)])
    return InlineKeyboardMarkup(result)
