# from app import app, db
from flask import render_template, Blueprint, request, redirect, g

from blogly.posts.post_model import Post
from blogly.tags.tag_model import Tag
from blogly.tags.tag_post_model import TagPost
from blogly.users.user_model import User

post_routes = Blueprint('post_routes', __name__,
                        url_prefix='/blogly',
                        static_folder="../posts")


#
# ADD POST: FORM (GET) AND PROCESSING (POST)
#
@post_routes.route('/users/<int:user_id>/posts/new', methods=['GET'])
def create_form_view(user_id):
    """
    Renders the Add Post form. Sends some special variables to the front-end:

    - method: the method to be sent by the form on click on the 'Save' button.
    - crud: the operation to configure the form.

    """
    post = Post({})
    post.user_id = user_id
    user = User.get(User, user_id)
    tags = Tag.all(Tag)
    return render_template('post_form.html',
                           method='POST',
                           crud='create',
                           page_title=f'{g.POSTS.ADD_PG} for {user.full_name()}',
                           post=post,
                           all_tags=tags)


@post_routes.route('/users/<int:user_id>/posts/new', methods=['POST'])
def post_add(user_id):
    """
    Treats the POST request to add the a new post.
    """
    dict_form = dict(request.form)
    dict_form['user_id'] = user_id
    post_id = Post.add(Post, dict_form)

    tag_keys = request.form.getlist("tag_keys")
    tag_post_list = [TagPost({'post_id': post_id, 'tag_id': tk}) for tk in tag_keys]
    TagPost.add_all(tag_post_list)
    return redirect(f'{g.USERS.PATH}/{dict_form["user_id"]}')


#
# POST DETAILS: VIEW, GO TO EDIT, GO TO DELETE
#
@post_routes.route('/posts/<int:post_id>')
def post_details_form_view(post_id):
    """
    Renders the form that shows the post details.


    From' Contexts
    ---------------
        User Details -> <Post title on the list>
    """
    # print(post.__repr__) # This is cool
    post = Post.get(Post, post_id)
    return render_template('post_view.html',
                           page_title=g.POSTS.VIEW_PG,
                           post=post)


#
# EDIT POST: FORM (GET) AND PROCESSING (POST)
#
@post_routes.route('/posts/<int:post_id>/edit')
def edit_view(post_id):
    """Renders Edit Post form. Sends some special variables to the front-end:

    - method: the method to be sent by the form on click on the 'Save' button.
    - crud: the operation to configure the form.
    """
    post = Post.get(Post, post_id)
    all_tags = Tag.all(Tag)
    post_tag_ids = post.get_tag_ids()
    return render_template('post_form.html',
                           method='POST',
                           crud='update',
                           page_title=g.POSTS.EDIT_PG,
                           post=post,
                           all_tags=all_tags,
                           post_tag_ids=post_tag_ids)


@post_routes.route('/posts/<int:post_id>/edit', methods=['POST'])
def edit_save(post_id):
    """
    Treats the POST request to update a post.
    """
    dict_form = dict(request.form)
    dict_form['id'] = post_id
    post = Post.get(Post, post_id)
    post.update(dict_form)

    tag_keys = request.form.getlist("tag_keys")
    # tag_post_list = [TagPost({'post_id': post_id, 'tag_id': tk}) for tk in tag_keys]
    TagPost.remove_from_post(post_id)
    post_tags = [TagPost({'tag_id': tag_id, 'post_id': post_id}) for tag_id in tag_keys]
    Tag.add_all(post_tags)
    return redirect(f'{g.USERS.PATH}/{post.user_id}')


#
# DELETE POST
#
@post_routes.route('/posts/<int:post_id>/delete', methods=['POST'])
def post_details_form_delete(post_id):
    """
    Treats the POST request to delete a post.
    """
    post = Post.get(Post, post_id)
    post.delete()
    return redirect(f'{g.USERS.PATH}/{post.user_id}')
