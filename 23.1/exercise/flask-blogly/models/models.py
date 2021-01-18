"""Models for Blogly."""

# from sqlalchemy_utils import URLType
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_db(app):
    """
    Sets and initializes the database for this app.
    """
    db.app = app;
    db.init_app(app)
