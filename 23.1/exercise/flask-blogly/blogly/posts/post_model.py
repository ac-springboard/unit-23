import os
from datetime import datetime

from flask import Blueprint

from blogly import db
from blogly.models import Models
# from blogly.users.user_model import User

post_model = Blueprint('post_model', __name__, template_folder='templates')


class Post(Models, db.Model):
    """
    - Initializes the posts table on postgres.
    - Represents a post from the posts table.
    """

    __tablename__ = 'posts'

    """
    Selects the schema to be used in the connected database.
    """
    __table_args__ = {'schema': os.environ.get('BLOGLY_SCHEMA_NAME')}

    # obj_dict = {}

    def __init__(self, obj_dict):
        # self.obj_dict = obj_dict
        self.update_columns(obj_dict)
        # Post.tags = db.relationship('Tag', secondary='tag_post', backref='posts')

    # COLUMNS

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True,
                   index=True)

    title = db.Column(db.String(50),
                      default='New Post',
                      nullable=False)
    content = db.Column(db.Text,
                        nullable=True)

    created_at = db.Column(db.DateTime,
                           default=datetime.now(),
                           nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('flask_blogly_test.users.id'))

    # RELATIONSHIPS

    user = db.relationship('User')
    # rel_tag_post = db.relationship('TagPost')
    rel_tags = db.relationship('Tag',
                               secondary='flask_blogly_test.tag_post',
                               backref='posts')

    def update_columns(self, dct):
        """
        Updates the data of this post from a dictionary.
        """
        self.id = dct.get('id', None)
        self.title = dct.get('title') or None
        self.content = dct.get('content') or None
        self.user_id = dct.get('user_id') or self.user_id
        self.created_at = dct.get('created_at') or self.created_at

        # print('test')
