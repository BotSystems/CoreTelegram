ROUTES = {
    'get_categories': 'shop-categories',
    'get_top_shops': 'shops?country={}&sort[rating]=DESC&page[limit]={}&offset[offset]={}',
    'get_shops_by_category': 'shops?filter[category_ids]={}&country={}',
    'get_shop_by_id': 'shops/{}',
    # 'get_shops': 'shops?country={}&page[offset]={}&page[limit]={}'
}
