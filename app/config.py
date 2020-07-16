import os


class Config(object):
    SECRET_KEY = '9ef03d70328e4bc88d84a0be93ce4499' # os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
