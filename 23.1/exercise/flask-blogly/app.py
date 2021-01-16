"""Blogly application."""

import os
from flask import Flask
from data_init.init_and_seed import AppInit
from models.models import db, setup_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql:///{os.environ['BLOGLY_DATABASE_NAME']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

setup_db(app)

if os.environ['BLOGLY_INIT'] == 'True':
    AppInit.drop_create(db)

if os.environ['BLOGLY_SEED'] == 'True':
    AppInit.insert_data(db)


