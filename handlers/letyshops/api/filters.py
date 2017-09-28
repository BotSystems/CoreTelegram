from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import BaseFilter


class WhatIsCashbackFilter(BaseFilter):
    def filter(self, message):
        return 'Что такое кэшбэк?' in message.text


class WantCashbackFilter(BaseFilter):
    def filter(self, message):
        return 'Хочу получать кэшбэк' in message.text


def what_is_cashback(bot, update, *args, **kwargs):
    text = 'Если коротко - это возврат части денег от покупки обратно. Желаешь узнать больше - переходи по ссылке, где тебя ждёт увлекательное путешествие в мир покупок и кэшбэка.'
    keyboard = [InlineKeyboardButton('Узнать больше', url='https://letyshops.ru/kak-rabotaet')]
    bot.send_message(chat_id=update.message.chat.id, text=text, reply_markup=InlineKeyboardMarkup([keyboard]))


def want_cashback(bot, update, *args, **kwargs):
    text = 'Отлично! Я сразу понял что в тебе есть что-то особенное. Давай же скорее зарегистрируемся.'
    keyboard = [InlineKeyboardButton('Зарегистрироваться', url='https://letyshops.ru/welcome-new-2')]
    bot.send_message(chat_id=update.message.chat.id, text=text, reply_markup=InlineKeyboardMarkup([keyboard]))
