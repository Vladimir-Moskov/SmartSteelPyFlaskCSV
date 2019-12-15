from app import db
from datetime import datetime

class SteelProcessing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, unique=True)
    temperature = db.Column(db.Float, index=True, unique=False)
    # duration = db.Column(db.Float) # duration in microseconds
    duration = db.Column(db.String(128))  # duration in microseconds

    def __repr__(self):
        return '<SteelProcessing: id:{}, timestamp:{}, temperature:{}, duration:{}>'.format(self.id, self.timestamp, self.temperature, self.duration)

    @staticmethod
    def headers():
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
        exists = SteelProcessing.query.filter_by(id=id).first()
        if not exists:
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
# smart_steel_technologies.py