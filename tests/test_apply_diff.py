from scripts.apply_diff import chunked


def test_chunked_splits_into_batches() -> None:
    items = frozenset(str(i) for i in range(5))

    batches = chunked(items, size=2)

    assert [len(b) for b in sorted(batches, key=len)] == [1, 2, 2]
    assert sorted(item for batch in batches for item in batch) == [
        "0",
        "1",
        "2",
        "3",
        "4",
    ]


def test_chunked_empty() -> None:
    assert chunked(frozenset(), size=100) == []


def test_chunked_smaller_than_batch_size() -> None:
    items = frozenset({"a", "b"})

    batches = chunked(items, size=100)

    assert len(batches) == 1
    assert set(batches[0]) == items
