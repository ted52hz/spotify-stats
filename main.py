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
# STREAMS_yyyy_mm_dd.csv
DAILY_STREAM_FILENAME = f'./Recreation/DailyStream/STREAMS_{
    get_datetime_today()}.csv'
TRACKS_INFO_FILENAME = './Data Storage/Tracks_info.csv'
ALBUM_INFO_FILENAME = "./Data Storage/Album_info.csv"
STREAM_FILENAME = "./Data Storage/STREAMS.csv"
DAILY_STREAM_FOLDER_PATH = './Recreation/DailyStream'

if __name__ == "__main__":

    # Scrapping Daily Stream
    scrape_spotify_songs(KWORB_ENDPOINT, DAILY_STREAM_FILENAME)

    # Extracting Tracks, Albums Info
    TRACK_ID_LIST = get_unique_values_from_column(STREAM_FILENAME, 'TRACK_ID')

    NEWEST_ID_LIST = get_unique_values_from_column(
        DAILY_STREAM_FILENAME, 'TRACK_ID')

    ALBUM_ID_LIST = get_unique_values_from_column(
        TRACKS_INFO_FILENAME, 'ALBUM_ID')

    New_song_flag = set(NEWEST_ID_LIST)-set(TRACK_ID_LIST)

    if New_song_flag:
        SAPI.get_info(TRACKS_API_ENDPOINT, TRACK_ID_LIST,
                      TRACKS_INFO_FILENAME, "tracks")

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
