"""CLI entrypoint: mirror the target playlist to the union of source playlists."""

from __future__ import annotations

import argparse
import os

from scripts.apply_diff import apply_diff
from scripts.auth import build_spotify_client
from scripts.compute_diff import compute_diff
from scripts.config import load_config
from scripts.fetch_tracks import get_playlist_track_uris


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    sp = build_spotify_client(
        client_id=os.environ["SPOTIFY_CLIENT_ID"],
        client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
        refresh_token=os.environ["SPOTIFY_REFRESH_TOKEN"],
    )

    desired: frozenset[str] = frozenset()
    for source_id in config.source_playlist_ids:
        desired |= get_playlist_track_uris(sp, source_id)

    current = get_playlist_track_uris(sp, config.target_playlist_id)
    diff = compute_diff(current, desired)
    apply_diff(sp, config.target_playlist_id, diff)

    print(f"added {len(diff.to_add)}, removed {len(diff.to_remove)}")


if __name__ == "__main__":
    main()
