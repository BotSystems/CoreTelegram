class Page:
    offset = None
    limit = None
    count = None

    def __init__(self, meta_data):
        self.limit = meta_data['limit']
        self.offset = meta_data['offset']
        self.count = meta_data['count']

    @property
    def get_offset(self):
        return int(self.offset)

    @property
    def get_limit(self):
        return int(self.limit)

    @property
    def get_count(self):
        return int(self.count)

    @property
    def has_prev(self):
        return self.offset + self.limit > self.limit

    @property
    def has_next(self):
        return self.count - (self.offset + self.limit) >= self.limit


if __name__ == '__main__':
    meta = {
        'count': 20,
        'limit': 10,
        'offset': 0
    }
    pager = Page(meta)
    print(pager.has_prev)
    print(pager.has_next)