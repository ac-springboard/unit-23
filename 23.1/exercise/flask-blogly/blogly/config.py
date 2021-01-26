import os


class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql:///{os.environ['BLOGLY_DATABASE_NAME']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    URL_ROOT = None  # This variable is dynamically updated
