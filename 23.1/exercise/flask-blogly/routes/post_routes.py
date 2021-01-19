# from app import app, db
from flask import render_template, Blueprint, redirect, request

from models.post_model import Post
from models.user_model import User

post_routes = Blueprint('post_routes', '__name__')


@post_routes.route('/posts')
def posts_view():
    posts = Post.query.all()
    return render_template('post_list.html',
                           page_title='Add Post',
                           posts=posts)
