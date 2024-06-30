from kworb_scraper import *
from spotify_scraper import *
from kworb_peak import *
from utils import *
from dotenv import load_dotenv
load_dotenv()

CLIEND_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
CONFIG_DATA = load_config('config', 'config.json')
ARTIST_ID = CONFIG_DATA['artist_id']
KWORB_ENDPOINT = CONFIG_DATA['endpoints']['kworb.net'].format(
    artist_id=ARTIST_ID)
KWORB_PEAK_ENDPOINT = CONFIG_DATA['endpoints']['peak'].format(
    artist_id=ARTIST_ID)
TRACKS_API_ENDPOINT = CONFIG_DATA['endpoints']['search_tracks']
ALBUM_API_ENDPOINT = CONFIG_DATA['endpoints']['search_album']
SAPI = SpotifyAPI(client_id, client_secret)
# STREAMS_yyyy_mm_dd.csv
DAILY_STREAM_FILENAME = f'./DailyStream/STREAMS_{get_datetime_today()}.csv'
TRACKS_INFO_FILENAME = './Data Storage/Tracks_info.csv'
ALBUM_INFO_FILENAME = "./Data Storage/Album_info.csv"
STREAM_FILENAME = "./Data Storage/STREAMS.csv"
PEAK_FILENAME = "./Data Storage/peaks.csv"
DAILY_STREAM_FOLDER_PATH = 'DailyStream'

if __name__ == "__main__":

    # Scrapping Daily Stream
    scrape_spotify_songs(KWORB_ENDPOINT, DAILY_STREAM_FILENAME)
    scrape_tracks_peak(KWORB_PEAK_ENDPOINT, PEAK_FILENAME)
    # Extracting Tracks, Albums Info
    TRACK_ID_LIST = get_unique_values_from_column(STREAM_FILENAME, 'TRACK_ID')

    NEWEST_ID_LIST_TRACK = get_unique_values_from_column(
        DAILY_STREAM_FILENAME, 'TRACK_ID')

    NEWEST_ID_LIST_PEAK = get_unique_values_from_column(
        PEAK_FILENAME, 'track_id')

    NEWEST_TRACK_ID_LIST = list(
        set(NEWEST_ID_LIST_TRACK).union(set(NEWEST_ID_LIST_PEAK)))

    New_song_flag = set(NEWEST_TRACK_ID_LIST)-set(TRACK_ID_LIST)

    if len(New_song_flag) > 0:
        SAPI.get_info(TRACKS_API_ENDPOINT, NEWEST_TRACK_ID_LIST,
                      TRACKS_INFO_FILENAME, "tracks")

        ALBUM_ID_LIST = get_unique_values_from_column(
            TRACKS_INFO_FILENAME, 'ALBUM_ID')

        SAPI.get_info(ALBUM_API_ENDPOINT, ALBUM_ID_LIST,
                      ALBUM_INFO_FILENAME, 'albums')
    else:
        print("No New songs found.")

    csv_files = [os.path.join(DAILY_STREAM_FOLDER_PATH, file) for file in os.listdir(
        DAILY_STREAM_FOLDER_PATH) if file.endswith('.csv')]
    dfs = [process_csv(file) for file in csv_files]
    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df.to_csv(STREAM_FILENAME, index=False)
    insert_pre_stream_df = insert_previous_daily_stream(STREAM_FILENAME)
    insert_pre_stream_df.to_csv(STREAM_FILENAME, index=False)
