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
        budda = User(first_name='Siddhārtha',
                     last_name='Gautama',
                     photo_url=None)
        jesus = User(first_name='Jesus',
                     last_name='Christ')
        krishna = User(first_name='Krishna',
                       last_name='Vasudeva',
                       photo_url=None)
        lahiru = User(first_name='Lahiru',
                      last_name='Gamathige',
                      photo_url=u'https://res-4.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1446050463/wle8mms7cc0leozu27fy.jpg')

        db.session.add(budda)
        db.session.add(jesus)
        db.session.add(krishna)
        db.session.add(lahiru)
        db.session.commit()
