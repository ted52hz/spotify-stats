import datetime
import csv
from datetime import timedelta
import pandas as pd

# Define datetime
today = datetime.datetime.today()
yesterday = today - timedelta(days=1)
today_file = f'./Transform/STREAMS_{today.strftime("%Y_%m_%d.csv")}'
yesterday_file = f'./Transform/STREAMS_{yesterday.strftime("%Y_%m_%d.csv")}'

yd = pd.read_csv(yesterday_file)
td = pd.read_csv(today_file)
# Merge the two DataFrames by Track_ID
merged_data = yd.merge(td, how='outer', on='TRACK_ID')
merged_data.rename(columns={'TOTAL_STREAM_y': 'TOTAL_STREAM',
                            'DAILY_STREAM_x': 'YESTERDAY_STREAM',
                            'DAILY_STREAM_y': 'TODAY_STREAM'}, inplace=True)
merged_data = merged_data.drop('TOTAL_STREAM_x', axis=1)
merged_data.fillna(0, inplace=True)
# print(merged_data)
merged_data.to_csv("./Load/STREAMS.csv", index=False)
