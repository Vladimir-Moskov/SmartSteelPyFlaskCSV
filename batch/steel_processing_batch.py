from app.models import SteelProcessing
from datetime import datetime
from app import db
from app.config import Config
from collections import namedtuple

def steel_processing_batch():
    SteelProcessing.query_delete_all()
    filepath = Config.BATCH_FILE_STEEL_PROCESSING
    with open(filepath) as file_processing:
        # the first line is headers
        line = file_processing.readline()
        # use namedtuple moderator to be able not sensitive to column order
        StlProc = namedtuple('StlProc', line)
        while line:
            line = file_processing.readline()
            if len(line) > 0:
                current_row = StlProc(*line.split(','))
                SteelProcessing.query_add_by_id(current_row.id, current_row.timestamp, current_row.temperature, current_row.duration)
            #break

if __name__ == '__main__':
    steel_processing_batch()
