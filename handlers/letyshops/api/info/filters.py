from telegram.ext import BaseFilter


class WhatIsCashbackFilter(BaseFilter):
    def filter(self, message):
        return 'Что такое кэшбэк?' in message.text


class WantCashbackFilter(BaseFilter):
    def filter(self, message):
        return 'Хочу получать кэшбэк' in message.text
