"""Models for Blogly."""
from typing import Type, TypeVar, Dict

from sqlalchemy import Integer

from blogly import db

T = TypeVar('T', bound='Models')


class Models:

    @staticmethod
    def all(cls: Type[T]):
        return cls.query.all()

    @staticmethod
    def get(cls: Type[T], type_id: Integer):
        return cls.query.get(type_id)

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

    def __repr__(self):
        return f"***** obj_dict -> {dict(self.__dict__)}"
