import os

from handlers.decorators import save_chanel_decorator
from handlers.letyshops.api.country.inline_keyboards import country_list_keyboard
from handlers.letyshops.api.country.models import Country
from models import find_chanel_by_chat

TOKEN = '{} {}'.format(os.getenv('SERVER_TOKEN_PREFIX'), os.getenv('SERVER_TOKEN_VALUE'))

COUNTRIES = (
    (u'Украина', 'ua'),
    (u'Россия', 'ru'),
    (u'Белоруссия', 'by'),
    (u'Казахстан', 'kz'),
)


@save_chanel_decorator
def send_countries(bot, update, *args, **kwargs):
    try:
        countries = []
        for (title, code) in COUNTRIES:
            countries.append(Country(title, code))

        markup = country_list_keyboard(countries)

        message = u"Выбери, пожалуйста страну для поиска, на этом все настройки будут оконченны:"
        return bot.send_message(update.message.chat.id, message, reply_markup=markup)
    except Exception as ex:
        print('Exception: ', ex)


@save_chanel_decorator
def set_country(bot, update, *args, **kwargs):
    try:
        selected_country = update.callback_query.data.split('.')[1] or 'ru'

        query = update.callback_query

        chanel = find_chanel_by_chat(query.message.chat)
        chanel.set_country(selected_country)

        default_country = u'России'
        countries = {
            'ua': u'Украины',
            'ru': default_country,
            'by': u'Белоруссии',
            'kz': u'Казахстана',
        }

        message = u"Настройки готовы, давай же проверим ТОП 10 магазинов {}.".format(
            countries.get(selected_country, default_country))
        return bot.send_message(query.message.chat_id, message)
    except Exception as ex:
        print('Exception: ', ex)
