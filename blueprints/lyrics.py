from flask import Blueprint, jsonify, request
from bs4 import BeautifulSoup
import requests
import pylrc

"""Lyrics Blueprint
This Blueprint Fetches Lyrics from https://megalobiz.com because by far its the most accurate one that I have come across.
"""

api = Blueprint(
    'lyrics',
    __name__,
    url_prefix='/lrc'
)

def parse_search_entities(soup):
    # Extract the number of downloads and views
    downloads_span = soup.find('span')
    downloads = downloads_span.get_text(strip=True).split('-')[1].replace('downloads', '').replace(',', '')
    views = downloads_span.get_text(strip=True).split('-')[0].replace('views', '').replace(',', '')

    # Extract the title
    title_a = soup.find('a', class_='entity_name')
    title = title_a.get_text(strip=True)
    link = title_a.get('href')

    # Extract a few lines of lyrics
    lyrics_div = soup.find('div', class_='details mid').find('div', class_='details')
    # lyrics_lines = lyrics_div.find_all('span')
    lyrics = lyrics_div.text

    # Return the extracted information
    return {
        'title': title,
        'downloads': int(downloads),
        'views': int(views),
        'lyrics': lyrics,
        'id': link
    }

@api.get('/search')
def search():
    """Lyrics Search
Search Lyrics from Megalobiz
Params:
- query : str : required : Query String 
    """
    query = request.args.get('query')
    url = f"https://www.megalobiz.com/search/all?qry={query.replace(' ', '+')}"
    soup = BeautifulSoup(requests.get(url).content)
    div = soup.find('div', {'id':'list_entity_container'})
    entities = div.find_all('div', class_="entity_full_member_box")
    results = list(map(
        parse_search_entities,
        entities
    ))
    results.sort(key=lambda x: x['downloads'], reverse=True)
    return jsonify(
        results
    )

@api.get('/lrc')
def get_lrc():
    """Fetch Lyrics
Fetch Lyrics from Megalobiz
Params:
- id : str: required : Id/URL of the lyrics
    """
    id = request.args.get('id')
    url = f"https://www.megalobiz.com/{id}"
    soup = BeautifulSoup(requests.get(url).content)
    dt = soup.find('div', class_="lyrics_details entity_more_info").find('span')
    lyrics = pylrc.parse(dt.text)
    lrc = {}
    for lyric in lyrics: lrc.update({lyric.time:lyric.text})
    return jsonify(
            lrc
        )