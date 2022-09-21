import pandas as pd


def read_csv(csv_name, column_name):
    data = pd.read_csv(csv_name)
    column_list = data[column_name].to_list()
    return column_list