from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def what_is_cashback(bot, update, *args, **kwargs):
    try:
        text = 'Если коротко - это возврат части денег от покупки обратно. Желаешь узнать больше - переходи по ссылке, где тебя ждёт увлекательное путешествие в мир покупок и кэшбэка.'
        keyboard = [InlineKeyboardButton('Узнать больше', url='https://letyshops.ru/kak-rabotaet')]
        return bot.send_message(chat_id=update.message.chat.id, text='*{}*'.format(text), reply_markup=InlineKeyboardMarkup([keyboard]), parse_mode='Markdown')
    except Exception as ex:
        print('Exception: ', ex)


def want_cashback(bot, update, *args, **kwargs):
    try:
        text = 'Отлично! Я сразу понял что в тебе есть что-то особенное. Давай же скорее зарегистрируемся.'
        keyboard = [InlineKeyboardButton('Зарегистрироваться', url='https://letyshops.ru/welcome-new-2')]
        return bot.send_message(chat_id=update.message.chat.id, text='*{}*'.format(text), reply_markup=InlineKeyboardMarkup([keyboard]), parse_mode='Markdown')
    except Exception as ex:
        print('Exception: ', ex)
