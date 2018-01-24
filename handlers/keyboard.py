from telegram import KeyboardButton, ReplyKeyboardMarkup


def build_keyboard():
    buttons = [[KeyboardButton('ТОП Магазинов')], [KeyboardButton('Категории'), KeyboardButton('Настройки')],
               [KeyboardButton('Что такое кэшбэк?'), KeyboardButton('Хочу получать кэшбэк!')]]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
