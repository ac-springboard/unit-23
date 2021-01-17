# from app import app, db
from models.models import User
from flask import render_template, Blueprint

routes = Blueprint('routes', '__name__')


@routes.route('/')
@routes.route('/list')
def users_view():
    users = User.query.all()
    return render_template('user_list.html',
                           page_title='Users',
                           users=users)


@routes.route('/users/<int:user_id>')
def details_view(user_id):
    user = User.query.get(user_id)
    return render_template('user_view.html',
                           page_title='User Details',
                           user=user)


@routes.route('/users/<int:user_id>/edit')
def edit_view(user_id):
    user = User.query.get(user_id)
    return render_template('user_form.html',
                           page_title='Edit User',
                           user=user)
