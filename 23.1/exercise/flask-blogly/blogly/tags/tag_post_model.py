import os

from flask import Blueprint

from blogly import db
from blogly.models import Models

tag_post_model = Blueprint('tag_post_model', __name__)


class TagPost(Models, db.Model):
    """
    - Initializes the tags table on postgres.
    - Represents the an tag from the tags table.
    """

    __tablename__ = 'tag_post'

    """
    Selects the schema to be used in the connected database.
    """
    schema_name = os.environ.get('BLOGLY_SCHEMA_NAME')
    __table_args__ = {'schema': schema_name}

    def __init__(self, obj_dict):
        # self.obj_dict = obj_dict
        self.update_columns(obj_dict)

    # COLUMNS

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)

    post_id = db.Column(db.Integer, db.ForeignKey(f'{schema_name}.posts.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey(f'{schema_name}.tags.id', ondelete='CASCADE'), nullable=False)

    def update_columns(self, dct):
        """
        Updates the data of this tag from a dictionary.
        """
        self.tag_id = dct.get('tag_id', None)
        self.post_id = dct.get('post_id', None)

    @staticmethod
    def remove_from_post(post_id):
        db.session.query(TagPost).filter(TagPost.post_id == post_id).delete()
        db.session.commit()
