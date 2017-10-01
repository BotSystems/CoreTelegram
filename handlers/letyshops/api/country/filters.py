from telegram.ext import BaseFilter


class CountryFilter(BaseFilter):
    def filter(self, message):
        return 'Настройки' in message.text
