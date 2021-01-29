import os

from flask import Blueprint

from blogly import db
from blogly.models import Models

user_model = Blueprint('user_model', __name__, template_folder='templates')


class User(Models, db.Model):
    """
    - Initializes the users table on postgres.
    - Represents the an user from the users table.
    """

    __tablename__ = 'users'

    """
    Selects the schema to be used in the connected database.
    """
    schema_name = os.environ.get('BLOGLY_SCHEMA_NAME')
    __table_args__ = {'schema': schema_name}

    def __init__(self, obj_dict):
        # self.obj_dict = obj_dict
        self.update_columns(obj_dict)

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True,
                   index=True)

    first_name = db.Column(db.String(50),
                           default='J',
                           nullable=False)

    last_name = db.Column(db.String(50),
                          default='Doe',
                          nullable=True)

    image_url = db.Column(db.String,
                          nullable=True,
                          default=u'https://i.pinimg.com/originals/4e/76/76/4e76765fda952b5d0243225a1c665874.jpg')

    posts = db.relationship('Post')

    def full_name(self):
        """
        Returns the full name of this user
        """
        return f"{self.first_name} {self.last_name}"

    def update_columns(self, dct):
        """
        Updates the data of this user from a dictionary.
        """
        self.id = dct.get('id', None)
        self.first_name = dct.get('first_name') or None
        self.last_name = dct.get('last_name') or None
        self.image_url = dct.get('image_url') or None
