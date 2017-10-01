from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import BaseFilter


# class WhatIsCashbackFilter(BaseFilter):
#     def filter(self, message):
#         return 'Что такое кэшбэк?' in message.text
#
#
# class WantCashbackFilter(BaseFilter):
#     def filter(self, message):
#         return 'Хочу получать кэшбэк' in message.text

class CategoryFilter(BaseFilter):
    def filter(self, message):
        return 'Категории' in message.text

def show_all(bot, update):
    reply_markup = InlineKeyboardMarkup(build_keyboard(CATEGORIES))
    update.message.reply_text(u"Выберите категорию для поиска", reply_markup=reply_markup)
