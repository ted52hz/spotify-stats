import os
import json
from datetime import datetime, timedelta
import csv
import pandas as pd


def load_config(foldername, filename):
    """
    Loads configuration data from a JSON file located in the 'config' directory.

    Returns:
    - dict: The loaded configuration data.
    """
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, foldername, filename)
    with open(file_path, 'r') as file:
        config_data = json.load(file)
    return config_data


def get_datetime_today():
    now = datetime.today()
    return now.strftime("%Y_%m_%d")


def get_unique_values_from_column(csv_file, column_name):
    unique_values = set()
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            unique_values.add(row[column_name])
    return unique_values


def process_csv(file):
    df = pd.read_csv(file)
    date_str = os.path.splitext(os.path.basename(file))[0].split('_')[1:]
    date = datetime.strptime('_'.join(date_str), '%Y_%m_%d')
    df['DATE'] = (date - timedelta(days=2)).strftime('%Y-%m-%d')
    return df


def insert_previous_daily_stream(file):
    df = pd.read_csv(file)
    df = df.sort_values(by='DATE')
    df['PREVIOUS_DAILY_STREAM'] = df.groupby(
        'TRACK_ID')['DAILY_STREAM'].shift(fill_value=0)
    return df
