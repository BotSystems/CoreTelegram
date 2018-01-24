from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def country_list_keyboard(country_list):
    country_keyboard = []
    countries = []

    for country in country_list:
        country_keyboard.append(InlineKeyboardButton(country.title, callback_data='set_country.' + country.code))
        if len(country_keyboard) == 2:
            countries.append(country_keyboard)
            country_keyboard = []

    return InlineKeyboardMarkup(countries)
