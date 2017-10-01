class Category:
    id = None
    title = None
    has_parent = None

    DISABLED = ('украина', 'россия', 'казахстан', 'беларусь')

    def __init__(self, id, title, has_parent):
        self.id = id
        self.title = title
        self.has_parent = has_parent

    @property
    def is_enabled(self):
        return self.title.lower() not in self.DISABLED and self.has_parent

    @staticmethod
    def filter(categories):
        return list(filter(lambda category: category.is_enabled, categories))

    @staticmethod
    def order(categories):
        return sorted(categories, key=lambda category: category.title)
