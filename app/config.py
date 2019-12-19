# flask application configuration variable

import os
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Setup Database driver/ connect to DB
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # batch job configurations
    BATCH_DIR = os.path.join(os.path.abspath(os.path.join(basedir, os.pardir)), 'resource')
    BATCH_FILE_STEEL_PROCESSING = os.path.join(BATCH_DIR, 'task_data.csv')

    @staticmethod
    def get_file_batch_steel_processing_error():
        """
        :return: file name for new error file
        """
        return os.path.join(Config.BATCH_DIR, '%s_task_data.error' % datetime.now().strftime("%m_%d_%Y_%H_%M_%S"))
