# import requests

# url = "http://127.0.0.1:5000/spotipy/track/6qrifdo7QINdPQr80IelGi?si=c30ff181edeb4230"
# data = requests.get(url)
# print(data.json())

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config

client_credentials_manager = (SpotifyClientCredentials(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET))
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

url = "https://open.spotify.com/album/2r3tG1S4XlpHM3z7xUp2lD?si=J36waD2cRKeIQezZSNYJXw"

album = spotify.album(url)
print(album)