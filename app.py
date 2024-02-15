# version : 0.0.2

from flask import Flask, jsonify, render_template, request
import spotipy
from spotipy.exceptions import SpotifyException
from spotipy.oauth2 import SpotifyClientCredentials
import config

app = Flask(__name__)

client_credentials_manager = SpotifyClientCredentials(
    config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET
)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/spotipy")
def spotipy():
    arg_type = request.args.get("type")
    arg_id = request.args.get("id")
    if arg_type == "track":
        if arg_id:
            try:
                url = f"https://open.spotify.com/track/{arg_id}"
                track = spotify.track(url)
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
                    "track_name": track_name,
                    "artists": artists,
                    "images": images,
                    "release_date": release_date,
                    "duration_ms": duration,
                }
                return jsonify(data)
            except SpotifyException as se:
                data = {"S002": {"error": str(se)}}
                return jsonify(data)
        else:
            data = {"S001": {"error": "No id is provided!"}}
            return jsonify(data)
    elif arg_type == "album":
        if arg_id:
            try:
                url = f"https://open.spotify.com/album/{arg_id}"
                album = spotify.album(url)
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
                    track_name = track["name"]
                    artists = ""
                    duration = track["duration_ms"]
                    for artist in track["artists"]:
                        fetched = f' {artist["name"]}'
                        if "Various Artists" not in fetched:
                            artists += fetched
                    song_dict = {
                        "track_name": track_name,
                        "artists": artists,
                        "duration_ms": duration,
                    }
                    tracks.append(song_dict)
                data = {
                    "album_name": album_name,
                    "album_by": album_by,
                    "images": images,
                    "label": label,
                    "release_date": release_date,
                    "total_tracks": total_tracks,
                    "tracks": tracks,
                }
                return jsonify(data)
            except SpotifyException as se:
                data = {"S002": {"error": str(se)}}
                return jsonify(data)
        else:
            data = {"S001": {"error": "No id is provided!"}}
            return jsonify(data)
    elif arg_type == "playlist":
        if arg_id:
            try:
                url = f"https://open.spotify.com/playlist/{arg_id}"
                playlist = spotify.playlist(url)
                playlist_name = playlist["name"]
                description = playlist["description"]
                followers = playlist["followers"]["total"]
                playlist_thumbnail = playlist["images"]
                owner = playlist["owner"]["display_name"]
                owner_profile_url = playlist["owner"]["external_urls"]["spotify"]
                owner_type = playlist["owner"]["type"]
                tracks = []
                for m_track in playlist["tracks"]["items"]:
                    track = m_track["track"]
                    track_name = track["name"]
                    artists = ""
                    duration = track["duration_ms"]
                    images = track["album"]["images"]
                    for artist in track["artists"]:
                        fetched = f' {artist["name"]}'
                        if "Various Artists" not in fetched:
                            artists += fetched
                    song_dict = {
                        "track_name": track_name,
                        "artists": artists,
                        "duration_ms": duration,
                        "images": images,
                    }
                    tracks.append(song_dict)
                data = {
                    "playlist_name": playlist_name,
                    "description": description,
                    "followers": followers,
                    "playlist_thumbnail": playlist_thumbnail,
                    "owner": owner,
                    "owner_profile_url": owner_profile_url,
                    "owner_type": owner_type,
                    "tracks": tracks,
                }
                return jsonify(data)
            except SpotifyException as se:
                data = {"S002": {"error": str(se)}}
                return jsonify(data)
        else:
            data = {"S001": {"error": "No id is provided!"}}
            return jsonify(data)
    else:
        data = {"S000": {"error": "invalid type!"}}
        return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
