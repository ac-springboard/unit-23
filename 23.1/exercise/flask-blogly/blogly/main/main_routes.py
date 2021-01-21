from flask import Blueprint, render_template

from blogly.users.user_model import User

main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/')
@main_routes.route('/list')
def main_home():
    """
    Render the User List template for both '/' and '/list' paths.
    """
    users = User.query.all()
    return render_template('user_list.html',
                           page_title='Users',
                           users=users)
