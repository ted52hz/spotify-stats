import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import re
import datetime

ARTIST_ID = "06HL4z0CvFAxyc27GXpf02"
URL = f"https://kworb.net/spotify/artist/{ARTIST_ID}_songs.html"
now = datetime.datetime.today()
today = now.strftime("%Y_%m_%d.csv")


def scrape_spotify_songs(url: str, filename) -> None:

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html5lib")
    links = soup.find_all("a", href=re.compile(
        "https://open.spotify.com/track/"))

    song_ids = []
    for link in links:
        song_id = link["href"][-22:]
        song_ids.append(song_id)

    df = pd.read_html(url, flavor="html5lib")[1]

    song_streams = df["Streams"].tolist()
    song_daily = df["Daily"].tolist()

    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["TRACK_ID", "TOTAL_STREAM", "DAILY_STREAM"])
        for i in range(len(song_ids)):
            song_entry = {
                "TRACK_ID": song_ids[i],
                "TOTAL_STREAM": song_streams[i],
                "DAILY_STREAM": song_daily[i],
            }
            csv_writer.writerow(song_entry.values())
    print("Done!")


if __name__ == "__main__":
    output = f"./Transform/STREAMS_{today}"
    scrape_spotify_songs(URL, output)
