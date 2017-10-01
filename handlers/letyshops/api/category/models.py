class Category:
    id = None
    title = None
    has_parent = None

    DISABLED = ('украина', 'россия', 'казахстан', 'беларусь')

    def __init__(self, id, title, has_parent):
        self.id = id
        self.title = title
        self.has_parent = has_parent

    def is_enabled(self):
        return self.title.lower() not in self.DISABLED and not self.has_parent

    @staticmethod
    def filter(categories):
        # list(filter(lambda category: int(category['parent_id']), category_list))
        return categories

    @staticmethod
    def order(categories):
        # sorted(category_list, key=lambda category: category['name'])
        return categories
