"""Read all track URIs off a Spotify playlist."""

from __future__ import annotations

import spotipy


def get_playlist_track_uris(sp: spotipy.Spotify, playlist_id: str) -> frozenset[str]:
    uris: set[str] = set()
    results = sp.playlist_items(
        playlist_id,
        fields="items(item(uri)),next",
        additional_types=("track",),
    )
    while results:
        for entry in results["items"]:
            track = entry.get("item")
            uri = track.get("uri") if track else None
            if uri and uri.startswith("spotify:track:"):
                uris.add(uri)
        results = sp.next(results) if results.get("next") else None

    return frozenset(uris)
