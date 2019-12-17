
# For simplicity - logging has not been added
# TODO: add real life logging
# https://www.scalyr.com/blog/getting-started-quickly-with-flask-logging/
# https://stackoverflow.com/questions/52728928/setting-up-a-database-handler-for-flask-logger

# For simplicity - unittests and integrasion tests has not been imolemented as well
# TODO: add real life tests with pytest

Data Base: sql in app.db fille
pip install -r requirements.txt
pip freeze > requirements.txt

$ pip install <package-name>
pip install flask-sqlalchemy
pip install flask-migrate

flask db init
flask db migrate -m "SteelProcessing table"
flask db migrate
flask db upgrade
