import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BATCH_DIR = os.path.join(os.path.abspath(os.path.join(basedir, os.pardir)), 'resource')
    BATCH_FILE_STEEL_PROCESSING = os.path.join(BATCH_DIR, 'task_data.csv')
