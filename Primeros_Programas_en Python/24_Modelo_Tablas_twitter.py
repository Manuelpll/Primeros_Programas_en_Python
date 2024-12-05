from datetime import datetime
from peewee import SqliteDatabase, Model, CharField, DateTimeField, ForeignKeyField, TextField

DATABASE = 'Twitter2.db'
database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()

class Relationship(BaseModel):
    from_user = ForeignKeyField(User, backref='relationships')
    to_user = ForeignKeyField(User, backref='related_to')

    class Meta:
        indexes = (
            (('from_user', 'to_user'), True),
        )

class Message(BaseModel):
    user = ForeignKeyField(User, backref='messages')
    content = TextField()
    pub_date = DateTimeField()
class Favorite(BaseModel):
    user = ForeignKeyField(User, backref='favorites')
    tweet= ForeignKeyField(Message, backref='favorites')

def create_tables():
    with database:
        database.create_tables(User,Relationship,Message,Favorite)

def insertarInfo():
    User.insert_many([
        {'username': 'Borja', 'password': 'Butanoo', 'email': 'borja.ticona@educa.madrid.org', 'join_date': datetime.today()},
        {'username': 'German', 'password': 'zzzzz', 'email': 'gescuderorodriguez@gmail.com', 'join_date': datetime(2021, 5, 12)},
        {'username': 'David', 'password': 'Anular22', 'email': 'david.pulgar@educa.madrid.org', 'join_date': datetime(2020, 3, 7)},
    ]).execute()

    borja = User.get(User.username == 'Borja')
    david = User.get(User.username == 'David')

    Message.create(user=borja, content='Tu no mete cabra saramanbiche', pub_date=datetime(2002, 9, 11))
    Message.create(user=david, content='Voy a recoger cartones', pub_date=datetime(2024, 11, 22))

    Relationship.create(from_user=borja, to_user=david)
    Relationship.create(from_user=david, to_user=User.get(User.username == 'German'))
 # query = Message.delete().where(Message.pub_date < datetime(2021, 5, 12))
if __name__ == '__main__':
   create_tables()
   insertarInfo()