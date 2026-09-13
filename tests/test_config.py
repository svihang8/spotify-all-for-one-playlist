from pathlib import Path

import pytest

from scripts.config import SyncConfig, load_config


def write_config(tmp_path: Path, content: str) -> Path:
    path = tmp_path / "config.yaml"
    path.write_text(content)
    return path


def test_load_config_valid(tmp_path: Path) -> None:
    path = write_config(
        tmp_path,
        """
        target_playlist_id: "target123"
        source_playlist_ids:
          - "sourceA"
          - "sourceB"
        """,
    )

    config = load_config(path)

    assert config == SyncConfig(
        target_playlist_id="target123",
        source_playlist_ids=frozenset({"sourceA", "sourceB"}),
    )


def test_load_config_missing_target(tmp_path: Path) -> None:
    path = write_config(
        tmp_path,
        """
        source_playlist_ids:
          - "sourceA"
        """,
    )

    with pytest.raises(ValueError, match="target_playlist_id"):
        load_config(path)


def test_load_config_missing_sources(tmp_path: Path) -> None:
    path = write_config(
        tmp_path,
        """
        target_playlist_id: "target123"
        source_playlist_ids: []
        """,
    )

    with pytest.raises(ValueError, match="source_playlist_ids"):
        load_config(path)
