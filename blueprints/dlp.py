from flask import Blueprint, jsonify, request, Response
from flask import redirect as rd
from ytmusicapi import YTMusic
from pytube import YouTube
import requests

api = Blueprint(
    'dlp',
    __name__
)

def generate_data_from_response(resp, chunk=2048):
    """
Generate data chunks from a response object.

Args:
- resp (requests.Response): The response object to generate data from.
- chunk (int): The chunk size in bytes (default is 2048).

Yields:
- bytes: Data chunk from the response.
    """
    for data_chunk in resp.iter_content(chunk_size=chunk):
        yield data_chunk

def serve_partial(url, range_header, mime, size=10485760):
    """
Serve partial content from a URL.

Args:
- url (str): The URL of the content.
- range_header (str): The Range header string specifying the byte range to fetch.
- mime (str): The MIME type of the content.
- size (int): The default size in bytes if until_bytes is not specified (default is 3145728).

Returns:
- flask.Response: The response object with the streamed content.
    """
    from_bytes, until_bytes = range_header.replace('bytes=', '').split('-')
    if not until_bytes:
        until_bytes = int(from_bytes) + size  # Default size is 5MB
        
    headers = {'Range': 'bytes=%s-%s' % (from_bytes, until_bytes)}
    r = requests.get(url, headers=headers, stream=True)

    rv = Response(generate_data_from_response(r), 206, mimetype=mime,
                  direct_passthrough=True)
    rv.headers.add('Content-Range', r.headers.get('Content-Range'))
    rv.headers.add('Content-Length', r.headers['Content-Length'])
    return rv

#TODO: Fix this Audio Streaming Messs :')

@api.route('/audio')
def fetch_audio():
    """
Fetch audio data from a YouTube video stream URL and serve it to the client.

Returns:
- flask.Response: The response object with the streamed audio data.
    """
    video_id = request.args.get('videoId')
    try:
        video = YouTube(f'https://music.youtube.com/watch?v={video_id}')
        stream = video.streams.filter(only_audio=True, abr="160kbps").first()
        if not stream:
            raise Exception('Audio stream not found')

        url = stream.url
        range_header = request.headers.get('Range', 'bytes=0-')
        return serve_partial(url, range_header, 'audio/webm', size=stream.filesize_approx)

    except Exception as e:
        return {'error': str(e)}, 500