from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import json
import csv

ARTIST_ID = "06HL4z0CvFAxyc27GXpf02"
url = f"https://kworb.net/spotify/artist/{ARTIST_ID}_songs.html"

song_urls = []
song_ids = []
song_streams = []
song_daily = []

# Request and parse the HTML content of the URL
response = requests.get(url)
soup = BeautifulSoup(response.content, "html5lib")

# Find all links to Spotify tracks
for link in soup.findAll("a", href=re.compile("https://open.spotify.com/track/")):
    # Extract the song URL and ID
    song_url = link["href"]
    song_id = link["href"][-22:]

    # Add the song URL and ID to the corresponding lists
    song_urls.append(song_url)
    song_ids.append(song_id)

df = pd.read_html (url, flavor='html5lib')
#print(df[1].columns) #Index(['Song Title', 'Streams', 'Daily'], dtype='object')

for i in df[1]['Streams']:
    song_streams.append(i)

for i in df[1]['Daily']:
    song_daily.append(i)  

# Create a list of dictionaries
song_data = []

for i in range(len(song_urls)):
    song_entry = {
        "song_urls": song_urls[i],
        "song_ids": song_ids[i],
        "song_streams": song_streams[i],
        "song_daily": song_daily[i]
    }

    song_data.append(song_entry)

# Create a CSV file writer object
csv_file = open("kworb.csv", "w", newline="")
csv_writer = csv.writer(csv_file)

# Write the title row to the CSV file
csv_writer.writerow(["song_urls", "song_ids","song_streams","song_daily"])

# Iterate over the list of dictionaries and write each row to the CSV file
for dictionary in song_data:
    csv_writer.writerow(dictionary.values())

# Close the CSV file writer object
csv_file.close()