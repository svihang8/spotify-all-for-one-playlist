"""Read all track URIs off a Spotify playlist."""

from __future__ import annotations

import spotipy


def get_playlist_track_uris(sp: spotipy.Spotify, playlist_id: str) -> frozenset[str]:
    uris: set[str] = set()
    results = sp.playlist_items(
        playlist_id,
        fields="items(track(uri)),next",
        additional_types=("track",),
    )
    while results:
        for item in results["items"]:
            track = item.get("track")
            if track and track.get("uri"):
                uris.add(track["uri"])
        results = sp.next(results) if results.get("next") else None

    return frozenset(uris)
