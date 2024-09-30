import os
import pandas as pd
input_dir = './inputs'


def list_paths_input():
    list_file_dir = os.listdir(input_dir)
    list_csv_files = []
    for file_dir in list_file_dir:
        if not file_dir.endswith('.csv'):
            continue

        complete_path = f'{input_dir}/{file_dir}'
        csv_read = pd.read_csv(complete_path, sep=';')
        names_headers = list(csv_read.head().columns)

        if names_headers[0] != 'destination' or names_headers[1] != 'subject' or names_headers[2] != 'body':
            continue

        list_csv_files.append(complete_path)

    return list_csv_files
