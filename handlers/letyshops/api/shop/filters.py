# -*-coding:utf-8;-*-

from telegram.ext import BaseFilter


class TopShopsFilter(BaseFilter):
    def filter(self, message):
        return 'ТОП Магазинов' in message.text
