# from app import app, db
from flask import render_template, Blueprint, redirect, request

from models.post_model import Post
from models.user_model import User

user_routes = Blueprint('user_user_routes', '__name__')


@user_routes.route('/')
@user_routes.route('/list')
def users_view():
    """
    Render the User List template for both '/' and '/list' paths.
    """
    users = User.query.all()
    return render_template('user_list.html',
                           page_title='Users',
                           users=users)


@user_routes.route('/users/new', methods=['GET'])
def create_form_view():
    """
    Renders the Add User form. Sends some special variables to the front-end:

    - method: the method to be sent by the form on click on the 'Save' button.
    - crud: the operation to configure the form.
    """
    user = User({})
    return render_template('user_form.html',
                           method='POST',
                           crud='create',
                           page_title='Add User',
                           user=user)


@user_routes.route('/users/new', methods=['POST'])
def create_view():
    """
    Treats the POST request to add the a new user.
    """
    dict_form = dict(request.form)
    User.add(User, dict_form)
    return redirect('/')


@user_routes.route('/users/<int:user_id>')
def details_form_view(user_id):
    """
    Renders the form that shows the user details.
    """
    user = User.query.get(user_id)
    return render_template('user_view.html',
                           page_title='User Details',
                           user=user,
                           posts=user.posts)


@user_routes.route('/users/<int:user_id>/edit')
def edit_view(user_id):
    """Renders Edit User form. Sends some special variables to the front-end:

    - method: the method to be sent by the form on click on the 'Save' button.
    - crud: the operation to configure the form.
    """
    user = User.query.get(user_id)
    return render_template('user_form.html',
                           method='POST',
                           crud='update',
                           page_title='Edit User',
                           user=user)


@user_routes.route('/users/<int:user_id>/edit/save', methods=['POST'])
def edit_save(user_id):
    """
    Treats the POST request to update a user.
    """
    dict_form = dict(request.form)
    dict_form['id'] = user_id
    user = User.query.get(user_id)
    user.update(dict_form)
    return redirect('/')


@user_routes.route('/users/<int:user_id>/delete', methods=['POST'])
def details_form_delete(user_id):
    """
    Treats the POST request to delete a user.
    """
    user = User.query.get(user_id)
    user.delete()
    return redirect('/')


@user_routes.route('/posts/new', methods=['GET'])
def create_post_form_view():
    """
    Renders the Post form. Sends some special variables to the front-end:

    - method: the method to be sent by the form on click on the 'Save' button.
    - crud: the operation to configure the form.
    """
    post = Post({})
    return render_template('user_form.html',
                           method='POST',
                           crud='create',
                           page_title='Add Post',
                           post=post)
