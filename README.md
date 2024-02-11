## Taylor Swift Spotify Stream Trend Dashboard
> In addition to providing insights into Taylor Swift's Spotify streaming trends, this project leverages the generated dashboard as a tool for informing and enriching social media blog posts. With the rise of data-driven content marketing strategies, the dashboard serves as a visual aid to accompany engaging narratives and analysis shared on various social media platforms.
## Overview
> With the increasing popularity of data-driven decision-making in the music industry, understanding streaming trends is crucial for artists and their teams. This project focuses on Taylor Swift's Spotify streaming trends, providing insights into her song popularity and audience engagement over time.
## Features
- **Web Scraping**: Data is crawled from a specified website to gather information about Taylor Swift's song daily stream counts.<br>
- **Spotify API Integration**: The project leverages the Spotify API to retrieve information for Taylor Swift's songs (Album Cover, Track Cover, Track-in-Album).<br>
- **Dashboard Visualization**: Displays the daily stream trend of Taylor Swift's songs in an interactive and informative dashboard.
## Project Structure
```
├── Data Storage
│   ├── Album_info.csv
│   ├── Album_info_filtered.csv
│   └── STREAMS.csv
│   └── Tracks_info.csv
├── DailyStream
│   ├── STREAMS_2024_01_02.csv
│   ├── STREAMS_2024_01_03.csv
│   └── ...
│   └── STREAMS_2024_02_11.csv
├── config
│   ├── config.json
├── utils.py
├── spotify_scraper.py
├── kworb_scraper.py
├── main.py
```
## Tableau
![image](https://github.com/khoaht312/spotify-stats/assets/69152064/024a9251-ef08-49de-8b3d-9c4b1099a807)

**Insights:**
- **Total Stream Over Time (2024)**:  Plot the total number of streams Taylor Swift has accumulated over time. This can provide a high-level view of her streaming performance and trends.
- **Highlight tracks**: Display the top streamed gainer tracks by Taylor Swift daily. This can help identify her most popular songs and fan favorites.
- **Stream Distribution by Album**: Visualize the distribution of streams across Taylor Swift's albums. This can highlight which albums are most popular among listeners.
- **Daily Stream Trends**: Track the daily streams of Taylor Swift's songs to identify any spikes or dips in streaming activity. This could be useful for understanding the impact of new releases, events,...
- 
### Acknowledgments

> The following resources were instrumental in the development of this project
- [Taylor Swift's albums discography](https://en.wikipedia.org/wiki/Taylor_Swift_albums_discography)
- [Kworb.net](https://kworb.net/) for providing song stream counts.
- [Spotify Web API](https://developer.spotify.com/documentation/web-api) for accessing to Spotify's data.
