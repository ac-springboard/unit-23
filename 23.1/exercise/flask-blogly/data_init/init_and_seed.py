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
        budda = User(first_name='Siddhārtha', last_name='Gautama')
        jesus = User(first_name='Jesus', last_name='Christ')
        krishna = User(first_name='Krishna', last_name='Vasudeva')
        lahiru = User(first_name='Lahiru', last_name='Gamathige')

        db.session.add(budda)
        db.session.add(jesus)
        db.session.add(krishna)
        db.session.add(lahiru)
        db.session.commit()
