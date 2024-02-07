import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import csv


def get_song_ids(url: str) -> list:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html5lib")
    links = soup.find_all("a", href=re.compile(
        "https://open.spotify.com/track/"))
    return [link["href"][-22:] for link in links]


def get_song_data(url: str) -> tuple:
    df = pd.read_html(url, flavor="html5lib")[1]
    return df["Streams"].tolist(), df["Daily"].tolist()


def write_song_data_to_csv(song_ids: list, song_streams: list, song_daily: list, filename: str) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["TRACK_ID", "TOTAL_STREAM", "DAILY_STREAM"])
        for track_id, total_stream, daily_stream in zip(song_ids, song_streams, song_daily):
            csv_writer.writerow([track_id, total_stream, daily_stream])


def scrape_spotify_songs(url: str, filename: str) -> None:
    song_ids = get_song_ids(url)
    song_streams, song_daily = get_song_data(url)
    write_song_data_to_csv(song_ids, song_streams, song_daily, filename)
    print("-[1]- Kworb_scraper.py (Write songs to csv file): Done")
