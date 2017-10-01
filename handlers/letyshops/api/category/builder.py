from handlers.letyshops.api.category.models import Category


def build_categories(categories: list) -> list:
    for category in categories:
        yield build_category(category)


def build_category(category_dict: dict) -> Category:
    id = category_dict.get('id')
    title = category_dict.get('name')
    has_parent = bool(int(category_dict.get('parent_id')))

    return Category(id, title, has_parent)
