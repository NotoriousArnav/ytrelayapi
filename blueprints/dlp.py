from flask import Blueprint, request, Response, jsonify
from flask import redirect as rd
from pytube import YouTube
from io import BytesIO
import requests

api = Blueprint(
    'dlp',
    __name__
)

def generate_data_from_response(resp, chunk=2048):
    """
    Generate data chunks from a response object and cache them using BytesIO.

    Args:
    - resp (requests.Response): The response object to generate data from.
    - chunk (int): The chunk size in bytes (default is 2048).

    Yields:
    - bytes: Data chunk from the response.
    """
    cached_data = BytesIO()
    for data_chunk in resp.iter_content(chunk_size=chunk):
        cached_data.write(data_chunk)
    cached_data.seek(0)
    
    total_size = cached_data.getbuffer().nbytes
    for start in range(0, total_size, chunk):
        cached_data.seek(start)
        yield cached_data.read(chunk)

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

    rv = Response(r, 206, mimetype=mime,
                  direct_passthrough=True)
    rv.headers.add('Content-Range', r.headers.get('Content-Range'))
    rv.headers.add('Content-Length', r.headers['Content-Length'])
    return rv

#TODO: Fix this Audio Streaming Messs :')
"""
This is Entirely fucked!!!!!!!!!!!
If we use videoId of a song that is Used by YT Music, the streaming link is IP Boud, and If we use regular videoId YT does not seem to care!
The Only Idea that has come to my mind since then is, separate the streams. If its a regular video ust fcking redirect to the streaming url else Stream it.
So, for now sadl the Client needs to use a Client Side software for this.
Some examples are:
yt-dlp: Python
ytdlp-nodejs: JS Backend
and maybe others.....
I guess VLC too has a good support for playing youtube videos by their youtube id, so maybe we can take a look at libvlc, but MPV solel relies on yt-dlp so Can't use MPV
"""


@api.route('/audio')
def fetch_audio():
    """
Fetch audio data from a YouTube video stream URL and serve it to the client.

Returns:
- flask.Response: The response object with the streamed audio data.
    """
    video_id = request.args.get('videoId')
    redirect = request.args.get('redirect')
    return_stream = request.args.get('return_stream')
    try:
        video = YouTube(f'https://www.youtube.com/watch?v={video_id}')
        stream = video.streams.filter(only_audio=True, abr="160kbps").first()
        if not stream:
            raise Exception('Audio stream not found')

        url = stream.url+'&ratebypass=yes'
        if redirect:
            return rd(url)
        elif return_stream:
            return jsonify(
                {
                    'url': url
                }
            )
        range_header = request.headers.get('Range', 'bytes=0-')
        return serve_partial(url, range_header, 'audio/webm', size=stream.filesize_approx)

    except Exception as e:
        return {'error': str(e)}, 500
