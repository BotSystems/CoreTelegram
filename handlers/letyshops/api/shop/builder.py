from handlers.letyshops.api.shop.models import Shop, Cashback


def build_cashback(cashback: dict) -> Cashback:
    value = cashback.get('value')
    unit = '%' if cashback.get('rate_type') == 'percent' else cashback.get('rate_type')
    waiting_days = cashback.get('cashback_waiting_days', 'Не указано')
    is_float = 'до' if cashback.get('is_floated') is True else ''

    return Cashback(value, unit, waiting_days, is_float)


def build_shops(shops: list) -> list:
    for shop in shops:
        yield build_shop(shop)


def build_shop(shop_dict: dict) -> Shop:
    id = shop_dict.get('id')
    name = shop_dict.get('name')
    url = shop_dict.get('url')
    logo = shop_dict.get('image')
    description = shop_dict.get('description')

    shop = Shop(id, logo, name, url, description)

    if ('cashback_waiting_days' in shop_dict and shop_dict['cashback_rate'] is not None):
        cashback_dict = shop_dict['cashback_rate']
        cashback_dict['cashback_waiting_days'] = shop_dict['cashback_waiting_days']
        cashback = build_cashback(shop_dict.get('cashback_rate', {}))

        shop.attach_cashback(cashback)

    return shop
