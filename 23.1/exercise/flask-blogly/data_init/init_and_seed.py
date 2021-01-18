from models.post_model import Post
from models.user_model import User


class AppInit:
    @staticmethod
    def drop_create(db):
        """
        (Re|Creates) all tables.
        """
        db.drop_all()
        db.create_all()
        db.session.commit()

    @staticmethod
    def insert_data(db):
        """
        Add test users
        """
        budda = User({'first_name': 'Siddhārtha',
                      'last_name': 'Gautama',
                      'image_url': None})
        jesus = User({'first_name': 'Jesus',
                      'last_name': 'Christ'})
        krishna = User({'first_name': 'Krishna',
                        'last_name': 'Vasudeva',
                        'image_url': None})
        lahiru = User({'first_name': 'Lahiru',
                       'last_name': 'Gamathige',
                       'image_url': 'https://res-4.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1446050463/wle8mms7cc0leozu27fy.jpg'})

        db.session.add(budda)
        db.session.add(jesus)
        db.session.add(krishna)
        db.session.add(lahiru)
        db.session.commit()

        post1 = Post({'title': 'Test Post 1', 'user_id': 1})
        post2 = Post({'title': 'Test Post 2', 'user_id': 1})

        db.session.add_all([post1, post2])
        db.session.commit()
