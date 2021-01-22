# from app import app, db
from flask import render_template, Blueprint, request, redirect

from blogly.posts.post_model import Post
from blogly.users.user_model import User

post_routes = Blueprint('post_routes', __name__, url_prefix='/blogly')


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


@post_routes.route('/users/<int:user_id>/posts/new', methods=['POST'])
def post_add(user_id):
    """
    Treats the POST request to add the a new post.
    """
    dict_form = dict(request.form)
    dict_form['user_id'] = user_id
    Post.add(Post, dict_form)
    return redirect(f'/blogly/users/{dict_form["user_id"]}')


@post_routes.route('/posts/<int:post_id>')
def post_details_form_view(post_id):
    """
    Renders the form that shows the post details.


    From' Contexts
    ---------------
        User Details -> <Post title on the list>
    """
    post = Post.get(Post, post_id)
    # print(post.__repr__) # This is cool
    return render_template('post_view.html',
                           page_title='Post Details',
                           post=post)


@post_routes.route('/posts/<int:post_id>/delete', methods=['POST'])
def post_details_form_delete(post_id):
    """
    Treats the POST request to delete a post.
    """
    post = Post.get(Post, post_id)
    post.delete()
    return redirect(f'/blogly/users/{post.user_id}')


@post_routes.route('/posts/<int:post_id>/edit')
def edit_view(post_id):
    """Renders Edit Post form. Sends some special variables to the front-end:

    - method: the method to be sent by the form on click on the 'Save' button.
    - crud: the operation to configure the form.
    """
    post = Post.get(Post, post_id)
    return render_template('post_form.html',
                           method='POST',
                           crud='update',
                           page_title='Edit Post',
                           post=post)


@post_routes.route('/posts/<int:post_id>/edit', methods=['POST'])
def edit_save(post_id):
    """
    Treats the POST request to update a post.
    """
    dict_form = dict(request.form)
    dict_form['id'] = post_id
    post = Post.get(Post, post_id)
    post.update(dict_form)
    return redirect(f'/blogly/users/{post.user_id}')


@post_routes.route('/posts/new', methods=['GET'])
def new():
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
