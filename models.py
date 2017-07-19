from peewee import *
import os

db = SqliteDatabase(os.path.join(os.getcwd(), 'lety_telegram.db'))


class Chanel(Model):
    chanel_id = IntegerField(unique=True)

    class Meta:
        database = db
