"""
    ORM - typical flask model setup
    ApplicationRequestLog for logs
"""
from app import db
from datetime import datetime
from typing import List, Optional, Any


class ApplicationRequestLog(db.Model):
    """
        Table to store user requests for "On each GET request, log that the data was requested (in the same database)"
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, index=True, unique=False, default=datetime.now())
    remote_addr = db.Column(db.String(100))
    url = db.Column(db.String(1000))
    method = db.Column(db.String(10))
    user_agent = db.Column(db.String(100))
    remote_user = db.Column(db.String(100))

    def __repr__(self) -> str:
        """
        Standard customization of class instance to string
        :return: string representation of object
        """
        return f'<ApplicationRequestLog: id:{self.id}, timestamp:{self.timestamp}, ' \
               f'remote_address:{self.remote_address}, url:{self.url}, remote_user:{self.remote_user},' \
               f' user_agent:{self.user_agent}>'

    @classmethod
    def query_get_all(cls):
        """
        just select all
        :return: all records from db (no paging or filtering)
        """
        return cls.query.all()

    @classmethod
    def query_delete_all(cls):
        """
            just delete all records from table - for testing purpose only

        """
        cls.query.delete()
        db.session.commit()

    @classmethod
    def query_add(cls, request):
        """
        add log record into DB, simple as possible
        :param request: real request - GET http from browser, web page
        :return: nothing
        """
        new_row = cls(remote_addr=request.remote_addr,
                      url=request.url,
                      method=request.method,
                      user_agent=str(request.user_agent),
                      remote_user=request.remote_user)
        db.session.add(new_row)
        db.session.commit()
