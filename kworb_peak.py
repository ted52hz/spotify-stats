import requests
import re
from bs4 import BeautifulSoup
import csv


def scrape_tracks_peak(url: str, filename: str) -> None:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html5lib")
    table = soup.find('table')
    data = []
    for row in table.find_all('tr'):
        cols = row.find_all(['td', 'th'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    pattern = r'\/track\/([a-zA-Z0-9]+)\.html'
    matches = soup.find_all('a', href=re.compile(pattern))
    track_ids = [re.search(pattern, match['href']).group(1)
                 for match in matches]

    for i in range(len(data)-1):
        data[i+1][1] = track_ids[i]

    headers = data[0][3:]
    data_rows = data[1:]

    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["track_id", "isoa2", "peak"])
        for row in data_rows:
            for i, value in enumerate(row[3:]):
                if value != '--':
                    csv_writer.writerow([row[1], headers[i], value])
                else:
                    continue
    print("- Extracting Peak: Done")


# scrape_tracks_peak(
#     'https://kworb.net/spotify/artist/06HL4z0CvFAxyc27GXpf02.html', 'a.csv')
