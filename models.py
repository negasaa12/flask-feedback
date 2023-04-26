
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

# username - a unique primary key that is no longer than 20 characters.
# password - a not-nullable column that is text
# email - a not-nullable column that is unique and no longer than 50 characters.
# first_name - a not-nullable column that is no longer than 30 characters.
# last_name - a not-nullable column that is no longer than 30 characters.


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    username = db.Column(db.String(length=20),
                         primary_key=True, unique=True, nullable=False)

    password = db.Column(db.String(length=50), nullable=False)

    email = db.Column(db.String(length=50), unique=True, nullable=False)

    first_name = db.Column(db.String(length=30), nullable=False)

    last_name = db.Column(db.String(length=30),  nullable=False)
