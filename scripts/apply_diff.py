"""Apply a TrackDiff to a playlist via the Spotify API."""

from __future__ import annotations

import spotipy

from scripts.compute_diff import TrackDiff

BATCH_SIZE = 100  # Spotify API limit per add/remove call


def chunked(items: frozenset[str], size: int) -> list[list[str]]:
    ordered = list(items)
    return [ordered[i : i + size] for i in range(0, len(ordered), size)]


def apply_diff(sp: spotipy.Spotify, playlist_id: str, diff: TrackDiff) -> None:
    for batch in chunked(diff.to_add, BATCH_SIZE):
        sp.playlist_add_items(playlist_id, batch)

    for batch in chunked(diff.to_remove, BATCH_SIZE):
        sp.playlist_remove_all_occurrences_of_items(playlist_id, batch)
