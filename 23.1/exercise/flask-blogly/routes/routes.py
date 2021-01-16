# from app import app, db
from models.models import User
from flask import render_template, Blueprint

routes = Blueprint('routes', '__name__')


@routes.route('/')
@routes.route('/list')
def root_view():
    users = User.query.all()
    return render_template('user_list.html',
                           page_title='User Listing',
                           users=users)
