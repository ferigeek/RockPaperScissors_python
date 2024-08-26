from peewee import *

db = SqliteDatabase(r'botDB.sqlite')

class User(Model):
    userID = IntegerField(primary_key=True)
    username = CharField()
    score = IntegerField()

    class Meta:
        database = db