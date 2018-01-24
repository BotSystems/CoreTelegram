ROUTES = {
    'get_categories': 'shop-categories?page[limit]={}&page[offset]={}',
    'get_top_shops': 'shops?country={}&sort[rating]=DESC&page[limit]={}&page[offset]={}',
    'get_shops_by_category': 'shops?page[limit]={}&page[offset]={}&filter[category_ids]={}&country={}&sort[rating]=DESC',
    'get_shop_by_id': 'shops/{}',
    'get_shop_by_name': 'shops?query[name]={}'
}
