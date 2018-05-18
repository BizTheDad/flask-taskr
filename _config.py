import os

basedir = os.path.abspath(os.path.dirname(__file__))

USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = os.urandom(24)

DATABASE = 'flask-taskr.db'
DATABASE_FOLDER = os.path.abspath(os.path.join(os.path.join(basedir, '..'),
                                               'flask-taskr-database'))
DATABASE_PATH = os.path.join(DATABASE_FOLDER, 'flask-taskr.db')
