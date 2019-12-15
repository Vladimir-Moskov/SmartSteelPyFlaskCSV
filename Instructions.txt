# TODO https://www.scalyr.com/blog/getting-started-quickly-with-flask-logging/
# https://stackoverflow.com/questions/52728928/setting-up-a-database-handler-for-flask-logger


$ pip install <package-name>
pip install flask-sqlalchemy
pip install flask-migrate
flask db init
flask db migrate -m "SteelProcessing table"
flask db migrate
flask db upgrade
