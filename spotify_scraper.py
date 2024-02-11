from utils import *
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import csv
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_token(self):
        auth_string = f"{self.client_id}:{self.client_secret}"
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": f"Basic {auth_base64}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}

        try:
            result = post(url, headers=headers, data=data)
            result.raise_for_status()  # Raise an exception for HTTP errors
            json_result = result.json()
            token = json_result["access_token"]
            return token
        except Exception as e:
            print(f"Error getting token: {e}")
            return None

    def get_auth_header(self, token):
        return {"Authorization": f"Bearer {token}"}

    def get_id_from_list(self, filename):
        try:
            with open(filename, "r") as csv_file:
                reader = csv.reader(csv_file)
                tracks_id = [row[0] for row in reader]
            return tracks_id[1:]
        except Exception as e:
            print(f"Error reading file: {e}")
            return []

    def get_info(self, endpoint, id_list, filename, flag="tracks"):
        token = self.get_token()
        if not token:
            print("Error: Failed to get token.")
            return

        try:
            with open(filename, "w", newline="", encoding="utf-8") as csv_file:
                csv_writer = csv.writer(csv_file)
                if flag == "tracks":
                    csv_writer.writerow(
                        ['TRACK_ID', 'TRACK_NAME', 'ALBUM_ID', 'TRACK_RELEASE_DATE', 'TRACK_COVER'])
                elif flag == "albums":
                    csv_writer.writerow(
                        ['ALBUM_ID', 'ALBUM_NAME', 'ALBUM_RELEASE_DATE', 'ALBUM_COVER'])

                for item_id in id_list:
                    url = endpoint.format(query=item_id)
                    headers = self.get_auth_header(token)
                    result = get(url, headers=headers)
                    result.raise_for_status()  # Raise an exception for HTTP errors
                    json_result = result.json()
                    if flag == "tracks":
                        info_entry = {
                            "TRACK_ID": json_result.get("id"),
                            "TRACK_NAME": json_result.get("name"),
                            "ALBUM_ID": json_result.get("album", {}).get("id"),
                            "TRACK_RELEASE_DATE": json_result.get("album", {}).get("release_date"),
                            "TRACK_COVER": json_result.get("album", {}).get("images", [{}])[0].get("url")
                        }
                    elif flag == "albums":
                        info_entry = {
                            "ALBUM_ID": json_result.get("id"),
                            "ALBUM_NAME": json_result.get("name"),
                            "RELEASE_DATE": json_result.get("release_date"),
                            "ALBUM_COVER": json_result.get("images", [{}])[0].get("url")
                        }
                    csv_writer.writerow(info_entry.values())
                print("- Extracting {} : Done".format(flag))
        except Exception as e:
            print(f"Error processing data: {e}")
