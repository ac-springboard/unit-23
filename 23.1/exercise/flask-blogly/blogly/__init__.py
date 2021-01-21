from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from blogly.config import Config

db = SQLAlchemy()


class Init:

    @staticmethod
    def create_app(config_class=Config):
        app = Flask(__name__, template_folder='templates')
        app.config.from_object(config_class)

        db.init_app(app)
        app.app_context().push()

        Init.register_blueprints(app)
        Init.create_tables()
        Init.insert_data()

        return app

    @staticmethod
    def register_blueprints(app):
        from blogly.main.main_routes import main_routes
        from blogly.users.user_routes import user_routes
        from blogly.posts.post_routes import post_routes

        app.register_blueprint(main_routes)
        app.register_blueprint(user_routes)
        app.register_blueprint(post_routes)

        from blogly.users.user_model import user_model
        from blogly.posts.post_model import post_model

        app.register_blueprint(user_model)
        app.register_blueprint(post_model)

    @staticmethod
    def create_tables():
        db.drop_all()
        db.create_all()
        db.session.commit()

    @staticmethod
    def insert_data():
        from blogly.users.user_model import User

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

        db.session.add_all([budda, jesus, krishna, lahiru])
        db.session.commit()

        from blogly.posts.post_model import Post

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
