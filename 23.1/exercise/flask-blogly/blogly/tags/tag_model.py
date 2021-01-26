import os

from flask import Blueprint, g

from blogly import db
from blogly.models import Models

tag_model = Blueprint('tag_model', __name__, template_folder='templates', static_folder='static')


class Tag(Models, db.Model):
    """
    - Initializes the tags table on postgres.
    - Represents the an tag from the tags table.
    """

    __tablename__ = 'tags'

    """
    Selects the schema to be used in the connected database.
    """
    __table_args__ = {'schema': os.environ.get('BLOGLY_SCHEMA_NAME')}

    def __init__(self, obj_dict):
        self.obj_dict = obj_dict
        self.update_columns(obj_dict)

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True,
                   index=True)

    name = db.Column(db.String(50),
                     default='New Tag',
                     unique=True,
                     nullable=False)

    rel_posts = db.relationship('Post',
                                secondary='flask_blogly_test.tag_post',
                                back_populates='rel_tags',
                                lazy='joined')

    def update_columns(self, dct):
        """
        Updates the data of this tag from a dictionary.
        """
        self.id = dct.get('id', None)
        self.name = dct.get('name', None)
