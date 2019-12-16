# typical flask model setup
from app import db
from datetime import datetime


class ApplicationRequestLog(db.Model):
    """
        Table to store user requests for "On each GET request, log that the data was requested (in the same database)"
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, index=True, unique=False)
    remote_addr = db.Column(db.String(100))
    url = db.Column(db.String(1000))
    method = db.Column(db.String(10))
    user_agent = db.Column(db.String(100))
    remote_user = db.Column(db.String(100))

    def __repr__(self):
        return '<ApplicationRequestLog: id:{}, timestamp:{}, remote_address:{}, remote_user:{}, user_agent:{}>'.\
            format(self.id, self.timestamp, self.remote_address, self.url, self.remote_user, self.user_agent)

    @staticmethod
    def query_get_all():
        return ApplicationRequestLog.query.all()

    @staticmethod
    def query_delete_all():
        ApplicationRequestLog.query.delete()
        db.session.commit()

    @staticmethod
    def query_add(request):
        timestamp_datetime = datetime.now()
        new_row = ApplicationRequestLog(timestamp=timestamp_datetime,
                                        remote_addr=request.remote_addr,
                                        url=request.url,
                                        method=request.method,
                                        user_agent=str(request.user_agent),
                                        remote_user=request.remote_user)
        db.session.add(new_row)
        db.session.commit()

    # TODO - change it to dictionary {header: field}
    @staticmethod
    def headers():
        """

        :return: list of headers names for ui
        """
        return ["ID", "TIMESTAMP", "IP", "URL", "METHOD", "AGENT", "USER"]


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

    def __repr__(self):
        return '<SteelProcessing: id:{}, timestamp:{}, temperature:{}, duration:{}>'.\
            format(self.id, self.timestamp, self.temperature, self.duration)

    # TODO - change it to dictionary {header: field}
    @staticmethod
    def headers():
        """

        :return: list of headers names for ui
        """
        return ["ID", "TIMESTAMP", "TEMPERATURE", "DURATION"]

    @staticmethod
    def query_get_all():
        return SteelProcessing.query.all()

    @staticmethod
    def query_delete_all():
        SteelProcessing.query.delete()
        db.session.commit()

    @staticmethod
    def query_add_by_id(id, timestamp, temperature, duration):
        # check if row with the same id already exists
        exists = SteelProcessing.query.filter_by(id=id).first()
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
            new_row = SteelProcessing(id=id, timestamp=timestamp_datetime, temperature=temperature, duration=duration)
            db.session.add(new_row)
            db.session.commit()
        return exists
