from flask import Blueprint, request, jsonify
from ytmusicapi.auth.oauth import OAuthCredentials
from ytmusicapi import YTMusic

oauth_credentials = OAuthCredentials()
anon_client = YTMusic()
api = Blueprint(
    "browsing",
    __name__
)

#TODO: Add Elaborative Documentation

# Route to get information about an artist
@api.route("/artist")
def get_artist():
    channelId = request.args.get("channelId")
    """Get Artist Information"""
    try:
        artist = anon_client.get_artist(channelId)
    except Exception as e:
        artist = {"error": str(e)}
    return jsonify(artist)

# Route to get the full list of an artist's albums or singles
@api.route("/artist_albums")
def get_artist_albums():
    channelId = request.args.get("channelId")
    params = request.args.get("params")
    limit = int(request.args.get("limit", 100))
    order = request.args.get("order")
    """Get Albums of the Artist"""
    try:
        albums = anon_client.get_artist_albums(channelId, params, limit=limit, order=order)
    except Exception as e:
        albums = {"error": str(e)}
    return jsonify(albums)

# Route to get information and tracks of an album
@api.route("/album")
def get_album():
    browseId = request.args.get("browseId")
    """Fetch an Album"""
    try:
        album = anon_client.get_album(browseId)
    except Exception as e:
        album = {"error": str(e)}
    return jsonify(album)

# Route to get an album's browseId based on its audioPlaylistId
@api.route("/album_browse_id")
def get_album_browse_id():
    audioPlaylistId = request.args.get("audioPlaylistId")
    """Get Browse Id of a Playlist"""
    try:
        browseId = anon_client.get_album_browse_id(audioPlaylistId)
    except Exception as e:
        browseId = {"error": str(e)}
    return jsonify({"browseId": browseId})

# Route to get metadata and streaming information about a song or video
@api.route("/song")
def get_song():
    videoId = request.args.get("videoId")
    signatureTimestamp = request.args.get("signatureTimestamp")
    try:
        song = anon_client.get_song(videoId, signatureTimestamp)
    except Exception as e:
        song = {"error": str(e)}
    return jsonify(song)

# Route to get related content for a song
@api.route("/song_related")
def get_song_related():
    browseId = request.args.get("browseId")
    try:
        related_content = anon_client.get_song_related(browseId)
    except Exception as e:
        related_content = {"error": str(e)}
    return jsonify(related_content)

# Route to get lyrics of a song or video
@api.route("/lyrics")
def get_lyrics():
    browseId = request.args.get("browseId")
    try:
        lyrics = anon_client.get_lyrics(browseId)
    except Exception as e:
        lyrics = {"error": str(e)}
    return jsonify(lyrics)
