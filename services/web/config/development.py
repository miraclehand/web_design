import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../data-dev.sqlite')

DEBUG=1
SECRET_KEY = 'top-secret!'
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
