from handlers.letyshops.api.category.models import Category


def build_category(category_dict):
    id = category_dict.get('id')
    title = category_dict.get('name')
    has_parent = bool(int(category_dict.get('parent_id')))

    return Category(id, title, has_parent)

def build_categories(categories):
    result = []
    for category in categories:
        result.append(build_category(category))

    return result
