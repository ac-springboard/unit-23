import os

from models.models import Models

db = Models.db


class User(Models, db.Model):
    """
    - Initializes the users table on postgres.
    - Represents the an user from the users table.
    """

    __tablename__ = 'users'

    """
    Selects the schema to be used in the connected database.
    """
    __table_args__ = {'schema': os.environ.get('BLOGLY_SCHEMA_NAME')}

    def __init__(self, user_dict):
        self.user_dict = user_dict
        self.update_columns(user_dict)

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

