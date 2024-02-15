from flask import Blueprint, jsonify, request, Response
from flask import redirect as rd
from pytube import YouTube
import requests

api = Blueprint(
    'dlp',
    __name__
)

def generate_data_from_response(resp, chunk=2048):
    for data_chunk in resp.iter_content(chunk_size=chunk):
        yield data_chunk

def serve_partial(url, range_header, mime, size=3145728):
    from_bytes, until_bytes = range_header.replace('bytes=', '').split('-')
    if not until_bytes:
        until_bytes = int(from_bytes) + size  # Default size is 3MB
        
    headers = {'Range': 'bytes=%s-%s' % (from_bytes, until_bytes)}
    r = requests.get(url, headers=headers, stream=True)

    rv = Response(generate_data_from_response(r), 206, mimetype=mime,
                  direct_passthrough=True)
    rv.headers.add('Content-Range', r.headers.get('Content-Range'))
    rv.headers.add('Content-Length', r.headers['Content-Length'])
    return rv

@api.route('/audio')
def fetch_audio():
    video_id = request.args.get('videoId')
    try:
        video = YouTube(f'https://music.youtube.com/watch?v={video_id}')
        stream = video.streams.filter(only_audio=True, abr="160kbps").first()
        if not stream:
            raise Exception('Audio stream not found')

        url = stream.url
        range_header = request.headers.get('Range', 'bytes=0-')
        return serve_partial(url, range_header, 'audio/webm')

    except Exception as e:
        return {'error': str(e)}, 500