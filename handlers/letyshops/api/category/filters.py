from telegram.ext import BaseFilter


class CategoryFilter(BaseFilter):
    def filter(self, message):
        return 'Категории' in message.text
