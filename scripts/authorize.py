"""One-time manual script: log in once, print a refresh token.

Run locally: uv run python scripts/authorize.py
Paste the printed refresh token into the SPOTIFY_REFRESH_TOKEN secret.
"""

from __future__ import annotations

import os

from spotipy.cache_handler import MemoryCacheHandler
from spotipy.oauth2 import SpotifyOAuth

from scripts.auth import REDIRECT_URI, SCOPE


def main() -> None:
    client_id = os.environ["SPOTIFY_CLIENT_ID"]
    client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]

    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        cache_handler=MemoryCacheHandler(),
        open_browser=True,
    )
    token_info = auth_manager.get_access_token(as_dict=True)
    print(token_info["refresh_token"])


if __name__ == "__main__":
    main()
