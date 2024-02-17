# import time
from flask import Blueprint, request, jsonify
from ytmusicapi.auth.oauth import OAuthCredentials
from ytmusicapi import YTMusic

oauth_credentials = OAuthCredentials()
anon_client = YTMusic()
api = Blueprint(
    "search",
    __name__
)

@api.route("/search")
def search():
    """Search API
Search Songs using YT Music API
Params:
query : Query string
filter : Filter for item types. Allowed values: songs, videos, albums, artists, playlists, 
community_playlists, featured_playlists, uploads. 
Default: Default search, including all types of items.
scope : Search scope. Allowed values: library, uploads. 
Default: Search the public YouTube Music catalogue
Changing scope from the default will reduce the number of settable filters. 
Setting a filter that is not permitted will throw an exception. 
For uploads, no filter can be set. 
For library, community_playlists and featured_playlists filter cannot be set.
limit : Number of search results to return Default: 20
ignore_spelling : Whether to ignore YTM spelling suggestions.
If True, the exact search term will be searched for, 
and will not be corrected. This does not have any effect when the filter is set to uploads.
Default: False, will use YTM’s default behavior of autocorrecting the search.
    """
    query = request.args.get("query")
    flt = request.args.get("filter")
    scope = request.args.get("scope")
    limit = int(request.args.get("limit", 20))
    ignore_spelling = request.args.get("ignore_spelling", False)

    try:
        results = anon_client.search(query=query, filter=flt, scope=scope, limit=limit, ignore_spelling=ignore_spelling)
    except Exception as e:
        results = e.args

    return jsonify(results)

@api.route("/search_suggestions")
def search_suggestions():
    """Search Suggestions
query : Query string
detailed_runs : Whether to return detailed runs of each suggestion. 
If True, it returns the query that the user typed and the remaining suggestion along with 
the complete text (like many search services usually bold the text typed by the user). 
Default: False, returns the list of search suggestions in plain text.
    """
    query = request.args.get("query")
    detailed_runs = request.args.get("detailed_runs", False)

    suggestions = anon_client.get_search_suggestions(query=query, detailed_runs=detailed_runs)

    return jsonify(suggestions)