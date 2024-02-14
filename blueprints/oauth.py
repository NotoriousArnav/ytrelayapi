from flask import Blueprint, request, jsonify
from ytmusicapi.auth.oauth import OAuthCredentials
import time

oauth_credentials = OAuthCredentials()
api = Blueprint(
    "api",
    __name__
)

@api.route("/connect")
def connect_ytmusic():
    # Step 1: Obtain authorization code
    auth_code_data = oauth_credentials.get_code()
    verification_url = auth_code_data.get("verification_url")
    user_code = auth_code_data.get("user_code")
    device_code = auth_code_data.get("device_code")

    # Display verification URL and user code to the user
    return jsonify(
            {
                "name":"Login to Google",
                "type":"popup",
                "link":f"{verification_url}?user_code={user_code}",
                "show": "true"
            },
            {
                "name":"Done",
                "type":"fetch",
                "link":f"/callback?device_code={device_code}",
                "show": "true"
            }
        )

@api.route("/callback")
def callback():
    # Step 2: Exchange authorization code for access token
    device_code = request.args.get("device_code")
    token_data = oauth_credentials.token_from_code(device_code)
    token_data['expires_at'] = int(time.time()) + int(token_data['expires_in'])

    return jsonify(
            token_data
        )
