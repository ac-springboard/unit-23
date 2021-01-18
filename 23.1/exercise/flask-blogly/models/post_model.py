import os
from datetime import datetime
from models.models import Models
from models.user_model import User

db = Models.db


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

    def __init__(self, post_dict):
        self.post_dict = post_dict
        self.update_columns(post_dict)

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True,
                   index=True)
    user = db.relationship('User')

    title = db.Column(db.String(50),
                      default='New Post',
                      nullable=False)
    content = db.Column(db.String,
                        nullable=True)

    created_at = db.Column(db.DateTime,
                           default=datetime.now(),
                           nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def update_columns(self, dct):
        """
        Updates the data of this post from a dictionary.
        """
        self.id = dct.get('id', None)
        self.title = dct.get('title') or None
        self.user_id = dct.get('user_id') or None
        self.created_at = dct.get('created_at') or None

    # def update(self, dct):
    #     """
    #     Updates the data of this post from a dictionary and commits the changes.
    #     """
    #     self.update_columns(dct)
    #     db.session.commit()
    #     return self

    # def delete(self):
    #     """
    #     Deletes this post.
    #     """
    #     db.session.delete(self)
    #     db.session.commit()

    # @staticmethod
    # def add(dct):
    #     """
    #     Adds a new post to the database, from the a dictionary.
    #     """
    #     post = Post(dct)
    #     db.session.add(post)
    #     db.session.commit()
    #     db.session.refresh(post)
    #     return post.id
