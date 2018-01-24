from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def show_categories_keyboard(categories):
    buttons = []
    for category in categories:
        buttons.append([InlineKeyboardButton(category.title, callback_data='show_category.{}'.format(category.id))])
    return buttons
