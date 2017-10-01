import re


class Cashback:
    value = None
    unit = None
    waiting_days = None
    is_float = None

    def __init__(self, value, unit, waiting_days, is_float):
        self.value = value
        self.unit = unit
        self.waiting_days = waiting_days
        self.is_float = is_float

    def is_exist(self):
        return all([self.value, self.unit])

    def __repr__(self):
        data = [self.is_float, self.value, self.unit, self.waiting_days]
        return '*Кэшбэк:* {} {}{}\n*Длительность ожидания кэшбэка:* {}'.format(*data)


class Shop:
    id = None
    logo = None
    name = None
    url = None
    description = None
    cashback = None

    def __init__(self, id, logo, name, url, description):
        self.id = id
        self.logo = logo
        self.name = name
        self.url = url
        self.description = description

    def attach_cashback(self, cashback: Cashback) -> 'Shop':
        self.cashback = cashback
        return self

    def normalize(self, result):
        result = re.sub(r'<[^>]*?>', '', result)
        result = re.sub(r'[*]', '', result)
        result = re.sub(r'&nbsp;', ' ', result)
        return result

    def render(self):
        return self.__repr__()

    def __repr__(self):
        if self.cashback.is_exist():
            data = [self.name, self.logo, self.cashback, self.normalize(self.description)]
            result = '[{}]({})\n{}\n*Дополнительная информация:* {}'.format(*data)
        else:
            data = [self.name, self.logo, self.normalize(self.description)]
            result = '[{}]({})\n*Дополнительная информация:* {}'.format(*data)

        return result
