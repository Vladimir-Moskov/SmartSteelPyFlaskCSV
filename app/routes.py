from app import app
from flask import render_template
from app import app
from app.models import SteelProcessing

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user="user")

@app.route('/steelProcessing')
def steelprocessing():
    return render_template('steelProcessing.html',
                           title='Steel Processing',
                           headers=SteelProcessing.headers(),
                           steelprocessing_all=SteelProcessing.query_get_all())