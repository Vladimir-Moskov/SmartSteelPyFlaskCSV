"""
    Use this script to clean data base in order to do full testing of data extract.
"""

from app.models.steelProcessing import SteelProcessing
from app.models.applicatonLog import ApplicationRequestLog


def clean_db() -> None:
    """
      Run clean DB by using Flask ecosystem - just call model interface
    """
    ApplicationRequestLog.query_delete_all()
    SteelProcessing.query_delete_all()

    
if __name__ == '__main__':
    clean_db()
