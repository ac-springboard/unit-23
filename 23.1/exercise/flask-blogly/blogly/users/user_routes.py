# from app import app, db
from flask import render_template, Blueprint, redirect, request

from blogly.users.user_model import User

user_routes = Blueprint('user_routes', __name__, url_prefix='/blogly')


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
                           page_title='Add User Form',
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
    return redirect(f'/blogly/users/{user_id}')


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
    user = User.query.get(user_id)
    return render_template('user_view.html',
                           page_title='User Details',
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
    user = User.query.get(user_id)
    return render_template('user_form.html',
                           method='POST',
                           crud='update',
                           page_title='Edit User',
                           user=user)


@user_routes.route('/users/<int:user_id>/edit/save', methods=['POST'])
def save(user_id):
    """
    Treats the POST request to update a user.
    """
    dict_form = dict(request.form)
    dict_form['id'] = user_id
    user = User.query.get(user_id)
    user.update(dict_form)
    return redirect(f'/blogly/users/{user_id}')


@user_routes.route('/users/<int:user_id>/delete', methods=['POST'])
def delete(user_id):
    """
    Treats the POST request to delete a user.
    """
    user = User.query.get(user_id)
    user.delete()
    return redirect('/blogly/list')
