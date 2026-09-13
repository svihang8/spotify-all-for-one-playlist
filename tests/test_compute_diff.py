from scripts.compute_diff import TrackDiff, compute_diff


def test_compute_diff_add_only() -> None:
    result = compute_diff(current=frozenset(), desired=frozenset({"a", "b"}))

    assert result == TrackDiff(to_add=frozenset({"a", "b"}), to_remove=frozenset())


def test_compute_diff_remove_only() -> None:
    result = compute_diff(current=frozenset({"a", "b"}), desired=frozenset())

    assert result == TrackDiff(to_add=frozenset(), to_remove=frozenset({"a", "b"}))


def test_compute_diff_mixed() -> None:
    result = compute_diff(
        current=frozenset({"a", "b"}), desired=frozenset({"b", "c"})
    )

    assert result == TrackDiff(to_add=frozenset({"c"}), to_remove=frozenset({"a"}))


def test_compute_diff_no_op() -> None:
    result = compute_diff(current=frozenset({"a", "b"}), desired=frozenset({"a", "b"}))

    assert result == TrackDiff(to_add=frozenset(), to_remove=frozenset())
