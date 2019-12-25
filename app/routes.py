"""
    Standard Flask routing - just simple url to function mapping
"""

from flask import request
from flask import render_template
from app import app
from app.models import SteelProcessing
from app.models import ApplicationRequestLog
from functools import wraps


def log_request(func):
    """
    user request logging decorator
    :param func: decorated function
    :return: decorator
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        ApplicationRequestLog.query_add(request)
        return func(*args, **kwargs)

    return decorated


@log_request
@app.errorhandler(404)
def not_found(e):
    """
         use template made by Colorlib (https://colorlib.com)
    :param e: request
    :return: error page wrapper
    """
    return render_template('404.html'), 404


@app.route('/')
@app.route('/index')
@log_request
def index():
    """
        Welcome page
    :return: page itself
    """
    return render_template('index.html', title='Welcome here')


@app.route('/steelProcessing')
@log_request
def steelprocessing():
    """
         Page with data from task_data.csv in order to solve
         Serve the database data (from `task_data.csv`) in a _simple_ html format
    :return: page itself
    """
    # TODO - it is nice to have paging/filtering over data
    return render_template('steelProcessing.html',
                           title='Steel Processing',
                           headers=SteelProcessing.headers(),
                           steelprocessing_all=SteelProcessing.query_get_all())


@app.route('/log')
@log_request
def log():
    """
         Page with data from user requests log in order to solve -
         "On each GET request, log that the data was requested (in the same database)"
    :return: page itself
    """
    # TODO - it is nice to have paging/filtering over data
    return render_template('applicationLog.html',
                           title='Application Log',
                           headers=ApplicationRequestLog.headers(),
                           logs_all=ApplicationRequestLog.query_get_all())
