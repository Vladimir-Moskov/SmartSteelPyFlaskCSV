from flask import request
from flask import render_template
from app import app
from app.models import SteelProcessing
from app.models import ApplicationRequestLog
from functools import wraps


# user request logging decorator
def log_request(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        ApplicationRequestLog.query_add(request)
        return func(*args, **kwargs)

    return decorated


@app.route('/')
@app.route('/index')
@log_request
def index():
    """
        Welcome page
    :return:
    """
    return render_template('index.html', title='Welcome here')


@app.route('/steelProcessing')
@log_request
def steelprocessing():
    """
         Page with data from task_data.csv in order to solve
         Serve the database data (from `task_data.csv`) in a _simple_ html format
    :return:
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
    :return:
    """
    # TODO - it is nice to have paging/filtering over data
    return render_template('applicationLog.html',
                           title='Application Log',
                           headers=ApplicationRequestLog.headers(),
                           logs_all=ApplicationRequestLog.query_get_all())
