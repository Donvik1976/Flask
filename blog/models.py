from flask_login import UserMixin
from sqlalchemy.orm import relationship

from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, nullable=False, default=False)


# class Article(db.Model):
#     __tablename__ = "articles"
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255))
#     text = db.Column(db.Text())
#     author = relationship('User')


