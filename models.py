import os
from os.path import join, dirname

from dotenv import load_dotenv
from peewee import PostgresqlDatabase, Model, IntegerField, CharField

if os.path.isfile('.env.settings'):
    dotenv_path = join(dirname(__file__), '.env.settings')
    load_dotenv(dotenv_path)

DATABASE_CREDENTIALS = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host ': os.getenv('DB_HOST'),
    'port ': os.getenv('DB_PORT')
}

db = PostgresqlDatabase(os.getenv('DB_NAME'), **DATABASE_CREDENTIALS)


def find_chanel_by_chat(chat):
    chanel, _ = Chanel.get_or_create(chanel_id=chat.id, defaults={'chanel_id': chat.id})
    return chanel


class Chanel(Model):
    chanel_id = IntegerField(unique=True)
    country = CharField(default='RU')

    def set_country(self, country):
        self.country = country
        self.save()

    class Meta:
        database = db
