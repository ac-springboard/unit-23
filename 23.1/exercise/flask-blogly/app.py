"""Blogly application."""

import os
from flask import Flask
from models.models import Models
from data_init.init_and_seed import AppInit
from routes.routes import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql:///{os.environ['BLOGLY_DATABASE_NAME']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.register_blueprint(routes)
Models.setup_db(app)

"""
Initializes (drop and create) the tables if the BLOGLY_INIT environment variable is set to True.
"""
if os.environ['BLOGLY_INIT'] == 'True':
    AppInit.drop_create(Models.db)

"""
Adds test values to the tables if the BLOGLY_SEED variable is set to True.
"""
if os.environ['BLOGLY_SEED'] == 'True':
    AppInit.insert_data(Models.db)
