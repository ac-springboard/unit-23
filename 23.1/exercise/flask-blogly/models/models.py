"""Models for Blogly."""

# from sqlalchemy_utils import URLType
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()


def setup_db(app):
    """Set and init the database for this app"""
    db.app = app;
    db.init_app(app)


class User(db.Model):
    """Initializes the User model"""

    __tablename__ = 'users'
    __table_args__ = {'schema': os.environ.get('BLOGLY_SCHEMA_NAME')}

    def __init__(self, user_dict):
        self.user_dict = user_dict
        self.update_columns(user_dict)

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True,
                   index=True)

    first_name = db.Column(db.String(50),
                           nullable=False)

    last_name = db.Column(db.String(50),
                          nullable=True)

    image_url = db.Column(db.String,
                          nullable=True,
                          default=u'https://i.pinimg.com/originals/4e/76/76/4e76765fda952b5d0243225a1c665874.jpg')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def update_columns(self, dct):
        self.id = dct.get('id', None)
        self.first_name = dct.get('first_name')
        self.last_name = dct.get('last_name')
        self.image_url = dct.get('image_url', None)

    def update(self, dct):
        self.update_columns(dct)
        db.session.commit()
        return self
