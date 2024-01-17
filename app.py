from flask import Flask, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re
import config

app = Flask(__name__)

client_credentials_manager = (SpotifyClientCredentials(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET))
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@app.route("/")
def home():
    return "Home!!"

@app.route("/spotipy/track/<string:id>")
def spotipy_track(id):
    track = spotify.track(id)
    track_name = track["name"]
    artists = ""
    images = track["album"]["images"]
    release_date = track["album"]["release_date"]
    duration = track["duration_ms"]
    for artist in track["artists"]:
                fetched = f' {artist["name"]}'
                if "Various Artists" not in fetched:
                    artists += fetched
    data = {
          "track_name":track_name,
          "artists":artists,
          "images":images,
          "release_date":release_date,
          "duration":duration
    }
    return jsonify(data)

@app.route("/spotipy/album/<string:id>")
def spotipy_album(id):
    album = spotify.album(id)
    album_name = album["name"]
    album_by = ""           
    for artist in album["artists"]:
            fetched = f' {artist["name"]}'
            if "Various Artists" not in fetched:
                album_by += fetched
    images = album["images"]
    label = album["label"]
    release_date = album["release_date"]
    total_tracks = album["total_tracks"]
    tracks = []
    for track in album["tracks"]["items"]:
        pass
    data = {"mode":"under test!!"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)