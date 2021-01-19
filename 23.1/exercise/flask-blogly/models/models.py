"""Models for Blogly."""
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from typing import Generic, Type, TypeVar, Dict

T = TypeVar('T', bound='Models')


class Models:
    db = SQLAlchemy()

    @staticmethod
    def setup_db(app):
        """
        Sets and initializes the database for this app.
        """
        Models.db.app = app;
        Models.db.init_app(app)

    @staticmethod
    def add(cls: Type[T], dict_arg: Dict):
        """
        Adds a new entry to the database, from the a dictionary.
        """
        t = cls(dict_arg)
        Models.db.session.add(t)
        Models.db.session.commit()
        Models.db.session.refresh(t)
        return t.id

    def delete(self):
        """
        Deletes this entry.
        """
        Models.db.session.delete(self)
        Models.db.session.commit()

    def update(self, dct):
        """
        Updates the data of this entry from a dictionary and commits the changes.
        """
        self.update_columns(dct)
        Models.db.session.commit()
        return self

