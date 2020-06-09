"""
    ORM - typical flask model setup
    SteelProcessing for records from given file with data
"""
from app import db
from datetime import datetime
from typing import Optional, Any


class SteelProcessing(db.Model):
    """
        Table SteelProcessing - store data model from file task_data.csv
    """
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, unique=False)
    temperature = db.Column(db.Float, index=True, unique=False)
    # TODO: convert timedelta to Float in order to save it in DB and store it in acceptable format but not as string
    # duration = db.Column(db.Float) # duration in microseconds
    duration = db.Column(db.String(128))  # store it as is - string for now

    def __repr__(self) -> str:
        """
            Standard customization of class instance to string
            :return: string representation of object
        """
        return f'<SteelProcessing: id:{self.id}, timestamp:{self.timestamp}, temperature:{self.temperature}, ' \
               f'duration:{self.duration}>'

    @classmethod
    def query_get_all(cls) -> None:
        """
          just select all
          :return: all records from db (no paging or filtering)
        """
        return cls.query.all()

    @classmethod
    def query_delete_all(cls) -> None:
        """
            just delete all records from table - for testing purpose only
        """
        cls.query.delete()
        db.session.commit()

    @classmethod
    def query_add_by_id(cls, row_id: int, timestamp: str, temperature: float, duration: str) -> Optional[Any]:
        """
           add log record into DB, simple as possible
        :param row_id: row data id
        :param timestamp: - timestamp field from data file
        :param temperature: - temperature field from data file
        :param duration: - duration field from data file

        :return: nothing
        """

        # TODO: here is example of implementation which is not scale very well,
        #  validation should be done at the same time as insertion
        #  just try except for  db.session.add(new_row) will be a better option,
        #  - in case of sql error "id has already exists" it will be captured and
        #  new_row can be returned as duplicated entity

        # check if row with the same id already exists
        exists = cls.query.filter_by(id=row_id).first()
        if not exists:
            # TODO: convert timedelta to Float in order to save it in DB
            # from datetime import timedelta
            # days_v_hms = duration.split('days')
            # hms = days_v_hms[1].split(':')
            # dt = timedelta(days=int(days_v_hms[0]), hours=int(hms[0]), minutes=int(hms[1]),
            #                         seconds=float(hms[2]))
            # duration_microsec = dt.microseconds
            #
            timestamp_datetime = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
            new_row = cls(id=row_id, timestamp=timestamp_datetime, temperature=temperature, duration=duration)
            db.session.add(new_row)
            db.session.commit()
        return exists
