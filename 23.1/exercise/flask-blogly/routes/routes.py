# from app import app, db
from models.models import User
from flask import render_template, Blueprint, redirect, request

routes = Blueprint('routes', '__name__')


@routes.route('/')
@routes.route('/list')
def users_view():
    users = User.query.all()
    return render_template('user_list.html',
                           page_title='Users',
                           users=users)


@routes.route('/users/new', methods=['GET'])
def create_form_view():
    user = User({})
    return render_template('user_form.html',
                           method='POST',
                           crud='create',
                           page_title='Add User',
                           user=user)


@routes.route('/users/new', methods=['POST'])
def create_view():
    dict_form = dict(request.form)
    User.add(dict_form)
    return redirect('/')


@routes.route('/users/<int:user_id>')
def details_form_view(user_id):
    user = User.query.get(user_id)
    return render_template('user_view.html',
                           page_title='User Details',
                           user=user)


@routes.route('/users/<int:user_id>/edit')
def edit_view(user_id):
    user = User.query.get(user_id)
    return render_template('user_form.html',
                           method='POST',
                           crud='update',
                           page_title='Edit User',
                           user=user)


@routes.route('/users/<int:user_id>/edit/save', methods=['POST'])
def edit_save(user_id):
    dict_form = dict(request.form)
    dict_form['id'] = user_id
    user = User.query.get(user_id)
    user.update(dict_form)
    return redirect('/')


@routes.route('/users/<int:user_id>/delete', methods=['POST'])
def details_form_delete(user_id):
    user = User.query.get(user_id)
    user.delete()
    return redirect('/')

