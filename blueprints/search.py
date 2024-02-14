from flask import Blueprint, request, jsonify
from ytmusicapi.auth.oauth import OAuthCredentials
from ytmusicapi import YTMusic
import time

oauth_credentials = OAuthCredentials()
anon_client = YTMusic()
api = Blueprint(
    "search",
    __name__
)

@api.route("/search")
def search():
    query = request.args.get("query")
    filter = request.args.get("filter")
    scope = request.args.get("scope")
    limit = int(request.args.get("limit", 20))
    ignore_spelling = request.args.get("ignore_spelling", False)

    try:
        results = anon_client.search(query=query, filter=filter, scope=scope, limit=limit, ignore_spelling=ignore_spelling)
    except Exception as e:
        results = e.args

    return jsonify(results)

@api.route("/search_suggestions")
def search_suggestions():
    query = request.args.get("query")
    detailed_runs = request.args.get("detailed_runs", False)

    suggestions = anon_client.get_search_suggestions(query=query, detailed_runs=detailed_runs)

    return jsonify(suggestions)