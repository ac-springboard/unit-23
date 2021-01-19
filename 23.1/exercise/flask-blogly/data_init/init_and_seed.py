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

        post_2_1 = Post({'title': 'הדיבר העשירי',
                         'content': 'עכשיו אני אומר לך לאהוב אחד את השני, כמו שאהבתי ',
                         'user_id': 2})
        post_3_1 = Post({'title': 'विश्वासों',
                         'content': 'एक आदमी अपनी मान्यताओं से बनता है। जैसा वह मानता है। तो वह बन जाता है।',
                         'user_id': 3})
        post_4_1 = Post({'title': 'මැක්සිමා ප්‍ර is ාව',
                         'content': 'මම යමක් කියන්නම් නමුත් ඔබට එය තේරෙන්නේ නැත.',
                         'user_id': 4})

        post_4_2 = Post({'title': 'For My Students',
                         'content': 'I wish my hair was growing as much as your knowledge.',
                         'user_id': 4})
        db.session.add_all([post_2_1, post_3_1, post_4_1, post_4_2])
        db.session.commit()
