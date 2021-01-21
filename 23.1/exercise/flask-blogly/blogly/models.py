"""Models for Blogly."""
from typing import Type, TypeVar, Dict

from blogly import db

T = TypeVar('T', bound='Models')


class Models:

    # @staticmethod
    # def setup_db(app):
    #     """
    #     Sets and initializes the database for this app.
    #     """
    #     Models.db.app = app;
    #     Models.db.init_app(app)

    @staticmethod
    def add(cls: Type[T], dict_arg: Dict):
        """
        Adds a new entry to the database, from the a dictionary.
        """
        t = cls(dict_arg)
        db.session.add(t)
        db.session.commit()
        db.session.refresh(t)
        return t.id

    def delete(self):
        """
        Deletes this entry.
        """
        db.session.delete(self)
        db.session.commit()

    def update(self, dct):
        """
        Updates the data of this entry from a dictionary and commits the changes.
        """
        self.update_columns(dct)
        db.session.commit()
        return self
