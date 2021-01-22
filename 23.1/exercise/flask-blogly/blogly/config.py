import os


class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql:///{os.environ['BLOGLY_DATABASE_NAME']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
