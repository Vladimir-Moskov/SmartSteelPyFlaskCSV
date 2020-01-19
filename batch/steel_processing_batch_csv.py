"""
    This is the better solution - with import csv for csv processing
    it Solves - Create an application that transfers `task_data.csv` to a database
    Solution works within Flask ecosystem.
"""

from csv import DictReader
from app.models import SteelProcessing
from app.config import Config


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

    with open(filepath, mode='r') as csv_file:
        try:
            # here is csv reader - he reads csv as list of OrderedDic
            csv_reader = DictReader(csv_file)
            # skip header and do data extraction from the second line till the end
            next(csv_reader, None)
            # process data line by line
            for line in csv_reader:
                try:
                    # TODO: its nice to have same to keep list row which has not been inserted because it
                    #  already exists
                    exists = SteelProcessing.query_add_by_id(line["id"],
                                                             line["timestamp"],
                                                             line["temperature"],
                                                             line["duration"])
                # TODO: specify which exceptions can be handled
                except Exception as error:
                    print(repr(error))
                    errors.append(line)
        except Exception as error:
            print(repr(error))

    # put all lines with errors in the file
    if len(errors) > 0:
        filepath = Config.get_file_batch_steel_processing_error()
        # overwrite previous content
        with open(filepath, 'w') as file_error:
            for item in errors:
                file_error.write("%s\n" % item)
    print("Data extraction has been completed.")


# run it as independent script / application - one time job
if __name__ == '__main__':
    steel_processing_batch()
