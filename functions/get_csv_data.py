import pandas as pd
from functions.read_input import *


def get_emails_array():
    list_csv_paths = list_paths_input()
    emails_array = []

    for csv_path in list_csv_paths:
        df = pd.read_csv(csv_path, names=['destination', 'subject', 'body'], sep=';', index_col=False)
        for index, row in df.iterrows():
            if index == 0:
                continue

            emails_array.append({'destination': row['destination'], 'subject': row['subject'], 'body': row['body']})

    return emails_array
