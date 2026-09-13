"""Compute what needs to change to mirror a set of desired tracks."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Diff:
    to_add: frozenset[str]
    to_remove: frozenset[str]


def compute_diff(current: frozenset[str], desired: frozenset[str]) -> Diff:
    return Diff(
        to_add=frozenset(desired - current),
        to_remove=frozenset(current - desired),
    )
