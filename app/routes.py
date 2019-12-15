from flask import request
from flask import render_template
from app import app
from app.models import SteelProcessing
from app.models import ApplicationRequestLog
from functools import wraps

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
    return render_template('index.html', title='Welcome here')

@app.route('/steelProcessing')
@log_request
def steelprocessing():
    return render_template('steelProcessing.html',
                           title='Steel Processing',
                           headers=SteelProcessing.headers(),
                           steelprocessing_all=SteelProcessing.query_get_all())

@app.route('/log')
@log_request
def log():
    return render_template('applicationLog.html',
                           title='Application Log',
                           headers=ApplicationRequestLog.headers(),
                           logs_all=ApplicationRequestLog.query_get_all())
