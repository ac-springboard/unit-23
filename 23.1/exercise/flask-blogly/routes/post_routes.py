# from app import app, db
from urllib import request

from flask import render_template, Blueprint, session, redirect

from models.post_model import Post

# from models.user_model import User
from models.user_model import User

post_routes = Blueprint('post_routes', '__name__')


@post_routes.route('/users/<int:user_id>/posts/new', methods=['GET'])
def create_form_view(user_id):
    """
    Renders the Add Post form. Sends some special variables to the front-end:

    - method: the method to be sent by the form on click on the 'Save' button.
    - crud: the operation to configure the form.
    """
    post = Post({})
    post.user_id = user_id
    user = User.query.get(user_id)
    return render_template('post_form.html',
                           method='POST',
                           crud='create',
                           page_title=f'Add Post for {user.full_name()}',
                           post=post)


@post_routes.route('/posts/new', methods=['POST'])
def create_view():
    """
    Treats the POST request to add the a new post.
    """
    dict_form = dict(request.form)
    Post.add(Post, dict_form)
    return redirect(f'/users/{dict_form["user_id"]}')
