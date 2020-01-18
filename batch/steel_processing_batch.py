"""
    This is the original solution - manual csv processing (bad idea - import csv or panda can do it better)
    Solve - Create an application that transfers `task_data.csv` to a database
    Solution works within Flask ecosystem.
"""


from app.models import SteelProcessing
from app.config import Config
from collections import namedtuple


def steel_processing_batch():
    """
    All in one place function - read from file and save in db

    :return: nothing for now
    """
    print("Data extraction has been started.")
    # uncomment this line to do another test
    # SteelProcessing.query_delete_all()
    errors = []  # get all lines from file which cant be inserted id DB - invalid data/format/values

    # batch file name and location
    # only for simplicity - only one file with hardcoded name can be handled
    # for real project usually do it with input/output dir, where all files in input folder should be processed
    # and moved to output folder
    filepath = Config.BATCH_FILE_STEEL_PROCESSING

    # open file with data and save all rows one by one
    # the process of db insertion  may be optimized by using
    # db.session.flush() after every row and db.session.commit() in the very end of process
    with open(filepath) as file_processing:
        # the first line is headers
        line = file_processing.readline()
        # use namedtuple moderator to be able not sensitive to column order
        StlProc = namedtuple('StlProc', line)

        while line:
            line = file_processing.readline()
            # basic validation - just to check is line empty or not
            if len(line) > 0:
                # if line can not be inserted - data error, It will be stored in error file
                try:
                    current_row = StlProc(*line.split(','))
                    # TODO: its nice to have same to keep list row which has not been inserted because it
                    #  already exists
                    exists = SteelProcessing.query_add_by_id(current_row.id,
                                                    current_row.timestamp,
                                                    current_row.temperature,
                                                    current_row.duration)
                # TODO: specify which exceptions can be handled
                except Exception as excp:
                    print(repr(excp))
                    errors.append(line)
    # put all lines with errors in the file
    if len(errors) > 0:
        filepath = Config.get_file_batch_steel_processing_error()
        # overwrite revious content
        with open(filepath, 'w') as file_error:
            for item in errors:
                file_error.write("%s\n" % item)
    print("Data extraction has been completed.")


# run it as independent script / application - one time job
if __name__ == '__main__':
    steel_processing_batch()
