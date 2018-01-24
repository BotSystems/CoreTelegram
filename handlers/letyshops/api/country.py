from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, ConversationHandler, MessageHandler, BaseFilter

from models import find_chanel_by_chat

COUNTRIES = (
    ('Украина', 'set_country.ua'),
    ('Россия', 'set_country.ru'),
    ('Белоруссия', 'set_country.by'),
    ('Казахстан', 'set_country.kz'),
)


# def build_keyboard(country_list):
#     countries = []
#     for (country, callback) in country_list:
#         country_keyboard = [InlineKeyboardButton(country, callback_data=callback)]
#         countries.append(country_keyboard)
#
#     return countries



def complete(bot, update):
    query = update.callback_query

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"Готово."
    )


# class CountryFilter(BaseFilter):
#     def filter(self, message):
#         return 'Настройки' in message.text


country_handler = ConversationHandler(
    entry_points=[MessageHandler(CountryFilter(), show_all)],
    states={
        'SAVE_COUNTRY': [CallbackQueryHandler(save_country)],
        'COMPLETE': [CallbackQueryHandler(complete)],
    },
    fallbacks=[],
    allow_reentry=True
)

if __name__ == '__main__':
    updater = Updater('403877811:AAFjD7RbEnRrNTQkqLyBOxQhx7OAnMpBc8Q')

    updater.dispatcher.add_handler(country_handler)
    updater.start_polling()
    updater.idle()
