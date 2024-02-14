from flask import Blueprint, jsonify, request
from flask import redirect as rd
from pytube import YouTube

api = Blueprint(
    'dlp',
    __name__
)

@api.get('/audio')
def fetch_audio():
    #TODO: Add Variable BitRate
    videoId = request.args.get('videoId')
    redirect = request.args.get('redirect')
    try:
        video = YouTube(f'https://youtube.com/watch?v={videoId}')
        stream = video.streams.filter(only_audio=True, abr="160kbps")[0] #Talking about this
        # Currently its stuck at 160kbps but I want to add Variable BitRate Support
        data = {'url':stream.url}
        if redirect:
            return rd(stream.url)
    except Exception as e:
        data = e.args

    return jsonify(data)