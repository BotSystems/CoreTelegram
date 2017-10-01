


def what_is_cashback(bot, update, *args, **kwargs):
    text = 'Если коротко - это возврат части денег от покупки обратно. Желаешь узнать больше - переходи по ссылке, где тебя ждёт увлекательное путешествие в мир покупок и кэшбэка.'
    keyboard = [InlineKeyboardButton('Узнать больше', url='https://letyshops.ru/kak-rabotaet')]
    bot.send_message(chat_id=update.message.chat.id, text=text, reply_markup=InlineKeyboardMarkup([keyboard]))


def want_cashback(bot, update, *args, **kwargs):
    text = 'Отлично! Я сразу понял что в тебе есть что-то особенное. Давай же скорее зарегистрируемся.'
    keyboard = [InlineKeyboardButton('Зарегистрироваться', url='https://letyshops.ru/welcome-new-2')]
    bot.send_message(chat_id=update.message.chat.id, text=text, reply_markup=InlineKeyboardMarkup([keyboard]))


def show_all(bot, update):
    reply_markup = InlineKeyboardMarkup(build_keyboard(COUNTRIES))
    update.message.reply_text(u"Выбери, пожалуйста страну для поиска, на этом все настройки будут оконченны:", reply_markup=reply_markup)

def save_country(bot, update):
    selected_country = update.callback_query.data.split('.')[1] or 'ru'

    query = update.callback_query

    chanel = find_chanel_by_chat(query.message.chat)
    chanel.set_country(selected_country)

    default_country = u'России'
    countries = {
        'ua': u'Украины',
        'ru':default_country,
        'by': u'Белоруссии',
        'kz': u'Казахстана',
    }

    bot.sendMessage(
        chat_id=query.message.chat_id,
        text=u"Настройки готовы, давай же проверим ТОП 10 магазинов {}.".format(countries.get(selected_country, default_country))
    )

@save_chanel_decorator
def choice_category(bot, update, *args, **kwargs):
    print(kwargs)
    country = kwargs['country']
    selected_category_id = update.callback_query.data.split('.')[1]

    query = update.callback_query

    shops = \
        json.loads(get_shop_by_category(AUTH_TOKENS_STORAGE, country, category_id=selected_category_id).content.decode("utf-8"))[
            'data']
    prepare_for_render = []

    for shop in shops:
        prepare_for_render.append((shop['name'], shop['id']))

    buttons = []
    for (shop_name, shop_id) in prepare_for_render:
        buttons.append([InlineKeyboardButton(shop_name, callback_data='show_shop_info.' + shop_id)])
    markup = InlineKeyboardMarkup(buttons, resize_keyboard=True)
    bot.send_message(chat_id=query.message.chat_id, text='Результат:', reply_markup=markup)


# def show_shop(bot, update):
#     try:
#         selected_shop_id = update.callback_query.data.split('.')[1]
#         query = update.callback_query
#
#         shop = get_shop_by_id(AUTH_TOKENS_STORAGE, shop_id = selected_shop_id)
#         if (shop.status_code == 200):
#             shop_full_data_json = json.loads(shop.content.decode("utf-8"))['data']
#             render_shop_answer(bot, query.message.chat_id, shop_full_data_json)
#     except Exception as ex:
#         print(ex)
#         # buttons = []
#         # buttons.append([InlineKeyboardButton('Перейти в магазин', url='http://example.com')])
#         # markup = InlineKeyboardMarkup(buttons, resize_keyboard=True)
#         # return bot.send_message(chat_id=query.message.chat_id, text=render_shop(shop_full_data), parse_mode='Markdown', reply_markup=markup)
#

@save_chanel_decorator
def find_shop_by_name(bot, update, *args, **kwargs):
    country = kwargs['country']
    bot.send_message(chat_id=update.message.chat.id, text='Запрос принят, ищу...')
    # shops = try_to_get_shops_from_cache(AUTH_TOKENS_STORAGE, country)
    shops = get_all_shops(AUTH_TOKENS_STORAGE, country)

    shop = find_shop_in_shops(str.strip(update.message.text), shops)
    if shop is None:
        return bot.send_message(chat_id=update.message.chat.id, text='Нет ничего такого :(')
    # подгружаем данные по ID
    shop_id = shop['id'] if isinstance(shop, dict) else None
    shop_full_response = get_shop_by_id(AUTH_TOKENS_STORAGE, shop_id=shop_id)
    if (shop_full_response.status_code == 200):
        shop_full_data_json = json.loads(shop_full_response.content.decode("utf-8"))['data']
        print(shop_full_data_json)
        render_shop_answer(bot, update.message.chat.id, shop_full_data_json)
    else:
        return bot.send_message(chat_id=update.message.chat.id, text='Нет ничего такого :(')

