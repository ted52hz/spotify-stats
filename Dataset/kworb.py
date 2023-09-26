from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import json
import csv

ARTIST_ID = "06HL4z0CvFAxyc27GXpf02"
url_song = f"https://kworb.net/spotify/artist/{ARTIST_ID}_songs.html"
url_album = f"https://kworb.net/spotify/artist/{ARTIST_ID}_albums.html"

def scrape_spotify_songs(url):
   response = requests.get(url)
   soup = BeautifulSoup(response.content, "html5lib")
   links = soup.findAll("a", href=re.compile("https://open.spotify.com/track/"))
   song_urls = []
   song_ids = []
   for link in links:
    song_url = link["href"]
    song_id = link["href"][-22:]
    song_urls.append(song_url)
    song_ids.append(song_id)
   df = pd.read_html(url, flavor="html5lib")
   song_streams = []
   song_daily = []
   for i in df[1]["Streams"]:
     song_streams.append(i)
     for i in df[1]["Daily"]:
       song_daily.append(i)
   song_data = []
   for i in range(len(song_urls)):
    song_entry = {
        "song_urls": song_urls[i],
        "track_id": song_ids[i],
        "song_streams": song_streams[i],
        "song_daily": song_daily[i],
    }
    song_data.append(song_entry)
    csv_file = open("kworb_track.csv", "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["song_urls", "track_id", "song_streams", "song_daily"])
    for dictionary in song_data:
      csv_writer.writerow(dictionary.values())
    csv_file.close()

def scrape_spotify_albums(url):
   response = requests.get(url)
   soup = BeautifulSoup(response.content, "html5lib")
   links = soup.findAll("a", href=re.compile("https://open.spotify.com/album/"))
   album_urls = []
   album_ids = []
   for link in links:
    album_url = link["href"]
    album_id = link["href"][-22:]
    album_urls.append(album_url)
    album_ids.append(album_id)
   df = pd.read_html(url, flavor="html5lib")
   album_name = []
   for i in df[0]["Album Title"]:
     print(i)
     album_name.append(i)
     album_data = []
   for i in range(len(album_urls)):
    album_entry = {
        "album_urls": album_urls[i],
        "album_ids": album_ids[i],
        "album_name":album_name[i]
    }
    album_data.append(album_entry)
    csv_file = open("kworb_album.csv", "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["album_urls", "album_ids","album_name"])
    for dictionary in album_data:
      csv_writer.writerow(dictionary.values())
    csv_file.close()


scrape_spotify_songs(url_song)
#scrape_spotify_albums(url_album)