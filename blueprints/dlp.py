from flask import Blueprint, jsonify, request
from flask import redirect as rd
from pytube import YouTube

api = Blueprint(
    'dlp',
    __name__
)

@api.get('/audio')
def fetch_audio():
    """
Fetch Playback URL of any YouTube Video.
Params:
- videoId : str : required : Video ID of the Video
- redirect: optional : redirect to the playback url, instead of returing in a JSON Response
    """
    #TODO: Add Variable BitRate
    videoId = request.args.get('videoId')
    redirect = request.args.get('redirect')
    try:
        video = YouTube(f'https://music.youtube.com/watch?v={videoId}')
        stream = video.streams.filter(only_audio=True, abr="160kbps").first().url #Talking about this
        # Currently its stuck at 160kbps but I want to add Variable BitRate Support
        data = {'url':stream}
        if redirect:
            return rd(stream)
    except Exception as e:
        data = e.args

    return jsonify(data)