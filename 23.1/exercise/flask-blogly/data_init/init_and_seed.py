from models.models import User


class AppInit:
    @staticmethod
    def drop_create(db):
        """(Re|Create) all tables"""
        db.drop_all()
        db.create_all()
        db.session.commit()

    @staticmethod
    def insert_data(db):
        """Add a default user"""
        fester = User(first_name='Fester', last_name='Bestertester')
        db.session.add(fester)
        db.session.commit()
