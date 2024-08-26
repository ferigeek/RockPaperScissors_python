from peewee import *
from models import *
from os import path
import asyncio

def create_tables():
    with db:
        db.create_tables([User])

def create_db():
    if path.exists('botDB.sqlite'):
        return
    else:
        with open('botDB.sqlite', 'w'):
            pass

async def check_user(userId, username):
    user = User.select().where(User.userID == userId)

    if not user:
        User.create(userID=userId, username=username, score=0)

async def add_score(userId):
    user = User.get(User.userID == userId)
    user.score += 1
    user.save()

create_db()
create_tables()