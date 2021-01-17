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
