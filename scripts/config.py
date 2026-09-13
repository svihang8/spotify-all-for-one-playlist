"""Load and validate the sync config file."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class SyncConfig:
    target_playlist_id: str
    source_playlist_ids: tuple[str, ...]


def load_config(path: Path | str) -> SyncConfig:
    data = yaml.safe_load(Path(path).read_text())

    target_playlist_id = data.get("target_playlist_id")
    if not target_playlist_id:
        raise ValueError("config missing 'target_playlist_id'")

    source_playlist_ids = data.get("source_playlist_ids")
    if not source_playlist_ids:
        raise ValueError("config missing non-empty 'source_playlist_ids'")

    return SyncConfig(
        target_playlist_id=target_playlist_id,
        source_playlist_ids=tuple(source_playlist_ids),
    )
