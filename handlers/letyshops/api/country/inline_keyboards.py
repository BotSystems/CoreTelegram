from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def country_list_keyboard(country_list):
    countries = []
    for country in country_list:
        country_keyboard = [InlineKeyboardButton(country.title, callback_data='set_country.' + country.code)]
        countries.append(country_keyboard)

    return InlineKeyboardMarkup(countries)
