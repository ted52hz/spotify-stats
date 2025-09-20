![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)

## Taylor Swift Spotify Stream Trend Dashboard
> In addition to providing insights into Taylor Swift's Spotify streaming trends, this project leverages the generated dashboard as a tool for informing and enriching social media blog posts. With the rise of data-driven content marketing strategies, the dashboard serves as a visual aid to accompany engaging narratives and analysis shared on various social media platforms.

## Metrics & Charts
1. **`Total Streams`**: This metric represents the cumulative number of times a song has been streamed on Spotify since its release or since Spotify started tracking it. It gives an overall indication of the song's long-term popularity and reach.

2. **`Daily Streams`**: Daily streams refer to the number of times a song is streamed on Spotify within a single day **(Friday 12:00 AM - Thursday 11:59 PM UTC)**. This metric provides insights into the immediate popularity and trend of a song.
 
3. **`Peak Streams`**: Peak streams indicate the highest number of streams a song has received within a specific timeframe, such as a day, a week, or a month. This metric highlights the peak of a song's popularity and can be useful for identifying key moments when the song gained significant traction, such as being featured on a popular playlist, going viral on social media, or being performed at a major event.

4. **`Daily Top Albums`**,**`Daily Top Songs`**: Spotify's rankings of the most streamed albums and tracks on a daily streams. These charts provide insights into what music is currently trending and most popular among Spotify users. Artists and listeners often pay close attention to these charts to gauge trends and discover new music.

5. **`Spotify Charted Tracks by country`**: The songs that have achieved notable popularity and have been officially recognized by Spotify Global 200 Charts (Which list 200 most streamed tracks over a certain period, such as a day, a week, or a month within a specific country or global). Spotify compiles charts that reflect the most streamed songs in various countries or regions.

## Notes (Based on my experience through working on this project)
1. **Many songs share the same name on music platforms like Spotify due to the existence of multiple versions or variations of the same song. This can occur for several reasons**:
- **Different Versions**: Artists often release multiple versions of the same song, such as radio edits, extended mixes, acoustic versions, remixes, or live recordings.
- **Explicit and Clean Versions**: Some songs/albums have both explicit and clean versions, with differences in lyrical content or language.
- **Inclusion in Deluxe Albums**: Songs may also appear multiple times under the same title when they are included in deluxe editions of albums. Deluxe versions often feature additional tracks, remixes, or bonus content alongside the standard album tracks.
> **Solution**: I create manually a file called `Album_info_filtered` to detect main albums and compile tracks for Daily top albums chart.

2. **Time to extract data**: The Spotify Daily charts are typically released before 12 PM EST (4 PM UTC) on the day following the chart period, while updates on kworb.net may occur after this time.

3. **Unfiltered streams**: This project's stream data demonstrates a variance of approximately 2% from Spotify's official chart, attributable to KWORB sourcing its data directly from Spotify Desktop.

4. **No stream data in the first two day of new tracks**: Kworb offers comprehensive data for songs that have been out for at least two days. For instance, the track mentioned displays total streams for its initial two days, with daily streams unavailable. To gauge the first day's streams, I rely on [Peak Data](https://kworb.net/spotify/artist/06HL4z0CvFAxyc27GXpf02.html) and then calculate the second day's streams by subtracting. This method proves valuable primarily for renowned artists featured on the Spotify Daily Chart Global. 

![image](https://github.com/khoaht312/spotify-stats/assets/69152064/740e81bf-4ee4-4de2-aa09-99c6c23fbbb2)

## Web Scraping and Extracting Data From API

![image](https://github.com/khoaht312/spotify-stats/assets/69152064/5c7a914b-3f83-4da9-bd8a-121984d34239)

[Edit Image](https://www.canva.com/design/DAGB_Z2emZo/DVVSmDlkqE5-ExBj3F183Q/edit?utm_content=DAGB_Z2emZo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

![image](https://github.com/khoaht312/spotify-stats/assets/69152064/627c7e84-0fc0-47ce-a873-7369d2f69829)

## Tableau:  [Link to Tableau Public](https://public.tableau.com/app/profile/tedhwang007/viz/TaylorSwiftSpotifyDashboard_17125561936560/v1)
![image](https://github.com/khoaht312/spotify-stats/assets/69152064/5d4e64bb-8621-4792-870e-44fe10b43d59)
![image](https://github.com/khoaht312/spotify-stats/assets/69152064/6cc13112-3d48-4bca-bc65-6cccd76f11be)
![image](https://github.com/khoaht312/spotify-stats/assets/69152064/31348bd6-50aa-4677-90cc-8218a061345d)


### Acknowledgments / Docs
> The following resources were instrumental in the development of this project
- `Taylor Swift's albums discography`- https://en.wikipedia.org/wiki/Taylor_Swift_albums_discography
- `Kworb.net`- https://kworb.net 
- `Spotify Web API`- https://developer.spotify.com/documentation/web-api
- `Spotify Charts` - https://charts.spotify.com/charts/overview/global
- `Spotify’s Social Media Strategy: Streaming Brilliant Content Globally` - https://keyhole.co/blog/spotify-social-media-strategy/
- `Audience stats - Charts` - https://support.spotify.com/us/artists/article/charts/
