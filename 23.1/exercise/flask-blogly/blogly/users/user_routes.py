# from app import app, db
from flask import render_template, Blueprint, redirect, request, g

from blogly.users.user_model import User

user_routes = Blueprint('user_routes', __name__,
                        url_prefix='/blogly',
                        template_folder="templates",
                        static_folder="../users")


@user_routes.route('/users/new', methods=['GET'])
def add_form():
    """
    Renders the Add User form. Sends some special variables to the front-end:
    - method: the method to be sent by the form on click on the 'Save' button.
    - crud: the operation to configure the form.

    'From' Context
    --------------
        Users -> Add User

    """
    user = User({})
    return render_template('user_form.html',
                           method='POST',
                           crud='create',
                           page_title=g.USERS.ADD_PG,
                           user=user)


@user_routes.route('/users/new', methods=['POST'])
def new():
    """
    Treats the POST request to add the a new post.

    'From' Context
    --------------
        Add User Form -> Save

    """
    dict_form = dict(request.form)
    user_id = User.add(User, dict_form)
    return redirect(f'{g.USERS.PATH}/{user_id}')


@user_routes.route('/users/<int:user_id>')
def details(user_id):
    """
    Renders the form that shows the user details.

    'From' Contexts
    ---------------
        Users -> <Name on the List>
        User Add Form -> Save or Cancel
        User Edit Form -> Save or Cancel
    """
    user = User.get(User, user_id)
    return render_template('user_view.html',
                           page_title=g.USERS.VIEW_PG,
                           user=user,
                           posts=user.posts)


@user_routes.route('/users/<int:user_id>/edit')
def edit_form(user_id):
    """Renders Edit User form. Sends some special variables to the front-end:

    - method: the method to be sent by the form on click on the 'Save' button.
    - crud: the operation to configure the form.

    'From' Contexts
    ---------------
        User View -> Edit
    """
    user = User.get(User, user_id)
    return render_template('user_form.html',
                           method='POST',
                           crud='update',
                           page_title=g.USERS.EDIT_PG,
                           user=user)


@user_routes.route('/users/<int:user_id>/edit/save', methods=['POST'])
def save(user_id):
    """
    Treats the POST request to update a user.
    """
    dict_form = dict(request.form)
    dict_form['id'] = user_id
    user = User.get(User, user_id)
    user.update(dict_form)
    return redirect(f'{g.USERS.PATH}/{user_id}')


@user_routes.route('/users/<int:user_id>/delete', methods=['POST'])
def delete(user_id):
    """
    Treats the POST request to delete a user.
    """
    user = User.get(User, user_id)
    user.delete()
    return redirect('/blogly/list')
