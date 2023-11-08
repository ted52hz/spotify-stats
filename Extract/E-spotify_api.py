from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import csv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
ARTIST_ID = "06HL4z0CvFAxyc27GXpf02"


def get_token():
    auth_string = str(client_id) + ":" + str(client_secret)
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def get_id_from_list(filename):
    tracks_id = []
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            track_id = row[0]
            tracks_id.append(track_id)
    return tracks_id[1:]


def get_tracks_info(token, track_id_list, filename):
    csv_file = open(filename, "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["TRACK_ID",
                         "TRACK_NAME",
                         "ALBUM_ID",
                         "ACOUSTICNESS",
                         "DANCEABILITY",
                         "ENERGY",
                         "INSTRUMENTALNESS",
                         "KEY",
                         "LIVENESS",
                         "LOUDNESS",
                         "MODE",
                         "SPEECHINESS",
                         "TEMPO",
                         "VALENCE",
                         "DURATION_MS"
                         ])
    for track_id in track_id_list:
        # Track_id, Track_name, Album_id
        url_1 = f"https://api.spotify.com/v1/tracks/{track_id}"
        # Audio Features
        url_2 = f"https://api.spotify.com/v1/audio-features/{track_id}"
        headers = get_auth_header(token)
        result_1 = get(url_1, headers=headers)
        result_2 = get(url_2, headers=headers)
        json_result_1 = json.loads(result_1.content)
        json_result_2 = json.loads(result_2.content)
        track_entry = {
            "TRACK_ID": track_id,
            "TRACK_NAME": json_result_1["name"],
            "ALBUM_ID": json_result_1["album"]["id"],
            "ACOUSTICNESS": json_result_2["acousticness"],
            "DANCEABILITY": json_result_2["danceability"],
            "ENERGY": json_result_2["energy"],
            "INSTRUMENTALNESS": json_result_2["instrumentalness"],
            "KEY": json_result_2["key"],
            "LIVENESS": json_result_2["liveness"],
            "LOUDNESS": json_result_2["loudness"],
            "MODE": json_result_2["mode"],
            "SPEECHINESS": json_result_2["speechiness"],
            "TEMPO": json_result_2["tempo"],
            "VALENCE": json_result_2["valence"],
            "DURATION_MS": json_result_2["duration_ms"]
        }
        csv_writer.writerow(track_entry.values())
    csv_file.close()
    print("Done!")


def get_album_info(token, album_id_list, filename):
    csv_file = open(filename, "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(
        ["ALBUM_ID", "ALBUM_NAME", "RELEASED_DATE", "ALBUM_IMAGE_URL"])
    for album_id in album_id_list:
        url = f"https://api.spotify.com/v1/albums/{album_id}"
        headers = get_auth_header(token)
        result = get(url, headers=headers)
        json_result = json.loads(result.content)
        album_entry = {
            "ALBUM_ID": json_result["id"],
            "ALBUM_NAME": json_result["name"],
            "RELEASED_DATE": json_result["release_date"],
            "ALBUM_IMAGE_URL": json_result["images"][0]["url"]
        }
        csv_writer.writerow(album_entry.values())
    csv_file.close()
    print("Done!")


if __name__ == "__main__":
    token = get_token()
    # tracks_id = get_id_from_list("./Load/STREAMS.csv")
    # get_tracks_info(token, tracks_id, "./Load/TRACKS.csv")
    albums_id = get_id_from_list("./Extract/album_filtered.csv")
    get_album_info(token, albums_id, "./Load/ALBUMS.csv")
