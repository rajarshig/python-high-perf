import csv
import sys
import os
import time


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


filename = 'data/org/kaggle.com_skylord_coronawhy_clean_metadata.csv'
temp_folder = 'data/temp'

def split_file(filename=filename):
    st = time.time()
    # full_file_path = os.path.join(CURRENT_DIR, filename)
    # file_name = os.path.splitext(full_file_path)[0]

    rows_per_csv = 5000 # int(sys.argv[2]) if len(sys.argv) > 2 else 5000

    split_filename_list = []
    with open(filename) as infile:
        reader = csv.DictReader(infile)
        header = reader.fieldnames
        rows = [row for row in reader]
        pages = []

        row_count = len(rows)
        start_index = 0
        # here, we slice the total rows into pages, each page having [row_per_csv] rows
        while start_index < row_count:
            pages.append(rows[start_index: start_index+rows_per_csv])
            start_index += rows_per_csv

        # for i, page in enumerate(pages):
        #     with open('{}_{}.csv'.format(filename, i+1), 'w+') as outfile:
        #         writer = csv.DictWriter(outfile, fieldnames=header)
        #         writer.writeheader()
        #         for row in page:
        #             writer.writerow(row)
        #     split_filename_list.append(filename)
        #     print('DONE splitting {} into {} files'.format(filename, len(pages)))
    
    et = time.time()
    time_diff = et - st
    return("Sec: {:.2f}".format(time_diff))
    
