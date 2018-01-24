import os


PAGER_STEP_SIZE = 5

TOP_QUERY = ':top:'
CATEGORY_QUERY = ':category:'
CATEGORIES_QUERY = ':categories:'

TOKEN = '{} {}'.format(os.getenv('SERVER_TOKEN_PREFIX'), os.getenv('SERVER_TOKEN_VALUE'))

DEFAULT_COUNTRY = u'России'

COUNTRIES = (
    ('🇺🇦', 'ua'),
    ('🇷🇺', 'ru'),
    ('🇧🇾', 'by'),
    ('🇰🇿', 'kz'),
)

COUNTRIES_TRANSLATE = {
    'ua': u'Украины',
    'ru': DEFAULT_COUNTRY,
    'by': u'Белоруссии',
    'kz': u'Казахстана',
}
