from flask import Blueprint, \
    render_template, g

from blogly.users.user_model import User

main_routes = Blueprint('main_routes',
                        __name__,
                        template_folder="templates",
                        url_prefix='/blogly',
                        static_folder="static")


@main_routes.route('/')
@main_routes.route('/list')
def main_home():
    """
    Render the User List template for both '/' and '/list' paths.
    """

    users = User.all(User)
    return render_template('user_list.html',
                           page_title='Users',
                           users=users)
