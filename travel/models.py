from cgitb import text
from email.mime import image
from locale import currency
from . import db
from flask_login import UserMixin
from datetime import datetime


class Destination(db.Model):
    __tablename__ = 'destinations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False, default='default.jpg')
    currency = db.Column(db.String(60), nullable=False, default='default.jpg')

    # relationships are pseudo attributes and are not columns in DB
    comments = db.relationship('Comment', backref='destination')

    def __repr__(self):
        return "<Name: {}, id: {}>".format(self.name, self.id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    # should be 128 in length to store hash
    password_hash = db.Column(db.String(255), nullable=False)
    usertype = db.Column(db.String(20), nullable=False, default='guest')

    comments = db.relationship('Comment', backref='user')

    def __repr__(self):
        return "<Name: {}, id: {}>".format(self.name, self.id)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.now())

    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return "<hotel id {} got a comment from user id {} that says: {} >".format(self.destination_id, self.userid, self.comment)
