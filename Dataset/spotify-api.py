from dotenv import load_dotenv
import os
import base64
from requests import post,get
import json
import csv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
ARTIST_ID = "06HL4z0CvFAxyc27GXpf02"

def get_token():
    auth_string = str(client_id)+ ":" + str(client_secret)
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type":"client_credentials"} 
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_album_ids(filename):
    album_ids = []
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            album_id = row[1]
            album_ids.append(album_id)
    return album_ids[1:]
  
def get_albums_tracks(token, albums_id_list):
    album_tracks = []

    for album_id in albums_id_list:
        # Get the album tracks from Spotify.
        url = f"https://api.spotify.com/v1/albums/{album_id}/tracks?market=US&limit=50"
        headers = get_auth_header(token)
        result = get(url, headers=headers)
        json_result = json.loads(result.content)

        # Add the album tracks to the list.
        for track in json_result["items"]:
            track_entry = {
                "album_id": album_id,
                "track_id": track["id"],
                "track_name": track["name"],
            }
            album_tracks.append(track_entry)

    csv_file = open("spotify_tracks_from_albums.csv", "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["album_id", "track_id","track_name"])
    for dictionary in album_tracks:
        csv_writer.writerow(dictionary.values())
    csv_file.close()

def get_track_ids(filename):
    track_ids = []
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            track_id = row[1]
            track_ids.append(track_id)
    return track_ids[1:]

def get_track_popularity(token, track_id_list):
    track_popularity = []
    for track_id in track_id_list:
        url = f"https://api.spotify.com/v1/tracks/{track_id}?market=US"
        headers = get_auth_header(token)
        result = get(url, headers=headers)
        json_result = json.loads(result.content)
        track_entry = {
            "track_id":json_result["id"],
            "popularity":json_result["popularity"]
        }
        track_popularity.append(track_entry)

    csv_file = open("spotify_tracks_popularity.csv", "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["track_id", "popularity"])
    for dictionary in track_popularity:
        csv_writer.writerow(dictionary.values())
    csv_file.close()

def get_track_audio_features(token, track_id_list):
    audio_features = []
    for track_id in track_id_list:
        url = f"https://api.spotify.com/v1/audio-features/{track_id}"
        headers = get_auth_header(token)
        result = get(url, headers=headers)
        json_result = json.loads(result.content)
        track_entry = {
            "track_id":json_result["id"],
            "acousticness":json_result["acousticness"],
            "danceability":json_result["danceability"],
            "energy":json_result["energy"],
            "instrumentalness":json_result["instrumentalness"],
            "loudness":json_result["loudness"],
            "tempo":json_result["tempo"],
            "valence":json_result["valence"]
        }
        audio_features.append(track_entry)

    csv_file = open("spotify_tracks_audio_features.csv", "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["track_id", "acousticness","danceability","energy","instrumentalness","loudness","tempo","valence"])
    for dictionary in audio_features:
        csv_writer.writerow(dictionary.values())
    csv_file.close()   

token = get_token()
#get_an_artist_albums(token)
#album_id = get_album_ids("kworb_album.csv")
#get_albums_tracks(token,album_id)
track_id = get_track_ids("kworb_track.csv")
get_track_popularity(token,track_id)
get_track_audio_features(token,track_id)