# clear data base in order to do full testing of data extract

from app.models import SteelProcessing
from app.models import ApplicationRequestLog

if __name__ == '__main__':
    ApplicationRequestLog.query_delete_all()
    SteelProcessing.query_delete_all()
