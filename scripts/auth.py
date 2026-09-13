"""Build an authenticated Spotify client from stored credentials.

Runtime auth only — no browser, no cache file. Suitable for CI.
"""

from __future__ import annotations

import spotipy
from spotipy.cache_handler import MemoryCacheHandler
from spotipy.oauth2 import SpotifyOAuth

REDIRECT_URI = "http://127.0.0.1:8888/callback"
SCOPE = "playlist-modify-public playlist-modify-private"


def build_spotify_client(
    client_id: str, client_secret: str, refresh_token: str
) -> spotipy.Spotify:
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        cache_handler=MemoryCacheHandler(),
        open_browser=False,
    )
    token_info = auth_manager.refresh_access_token(refresh_token)
    return spotipy.Spotify(auth=token_info["access_token"])
