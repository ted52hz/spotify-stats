from kworb_scraper import *
from spotify_scraper import *
from utils import *
from dotenv import load_dotenv
load_dotenv()

CLIEND_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

CONFIG_DATA = load_config('config', 'config.json')

ARTIST_ID = CONFIG_DATA['artist_id']

KWORB_ENDPOINT = CONFIG_DATA['endpoints']['kworb.net'].format(
    artist_id=ARTIST_ID)

TRACKS_API_ENDPOINT = CONFIG_DATA['endpoints']['search_tracks']

ALBUM_API_ENDPOINT = CONFIG_DATA['endpoints']['search_album']

SAPI = SpotifyAPI(client_id, client_secret)

if __name__ == "__main__":
    """
    extract most daily stream -> get track_id -> 500 track info -> get album_id -> get album info
    Track_info.csv
    Album_info.csv
    Album_info_filtered.csv
    Streams.csv
    """
    # DAILY_STREAM_FILENAME = f'./DailyStream/STREAMS_{get_datetime_today()}.csv'  # STREAMS_yyyy_mm_dd.csv

    # TRACKS_INFO_FILENAME = 'Tracks_info.csv'

    # ALBUM_INFO_FILENAME = "Album_info.csv"

    # scrape_spotify_songs(KWORB_ENDPOINT, DAILY_STREAM_FILENAME)

    # TRACK_ID_LIST = get_unique_values_from_column(DAILY_STREAM_FILENAME, 'TRACK_ID')

    # SAPI.get_info(TRACKS_API_ENDPOINT, TRACK_ID_LIST,TRACKS_INFO_FILENAME, "tracks")

    # ALBUM_ID_LIST = get_unique_values_from_column(TRACKS_INFO_FILENAME, 'ALBUM_ID')

    # SAPI.get_info(ALBUM_API_ENDPOINT, ALBUM_ID_LIST,ALBUM_INFO_FILENAME, 'albums')

    DAILY_STREAM_FOLDER_PATH = './DailyStream'
    csv_files = [os.path.join(DAILY_STREAM_FOLDER_PATH, file) for file in os.listdir(
        DAILY_STREAM_FOLDER_PATH) if file.endswith('.csv')]
    dfs = [process_csv(file) for file in csv_files]
    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df.to_csv('STREAMS.csv', index=False)
