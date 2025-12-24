import pytest
from src.sorts import (
    bubble_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
    heap_sort,
)


def is_sorted(a):
    return all(a[i] <= a[i + 1] for i in range(len(a) - 1))


def test_bubble_sort_basic():
    arr = [5, 3, 1, 4, 2]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]
    assert is_sorted(bubble_sort(arr))


def test_quick_sort_basic():
    arr = [10, -1, 3, 7, 0]
    assert quick_sort(arr[:]) == sorted(arr)
    assert is_sorted(quick_sort(arr))


def test_heap_sort_basic():
    arr = [7, 2, 9, -3, 0, 5]
    assert heap_sort(arr) == sorted(arr)
    assert is_sorted(heap_sort(arr))


def test_counting_sort_with_negatives():
    arr = [3, -1, 2, -1, 0, 3]
    assert counting_sort(arr) == sorted(arr)
    assert is_sorted(counting_sort(arr))
    with pytest.raises(TypeError):
        counting_sort([1.1, 2.2, 3.3])


def test_radix_sort_with_negatives():
    arr = [170, -45, 75, -90, 802, 24, 2, 66]
    assert radix_sort(arr) == sorted(arr)
    assert is_sorted(radix_sort(arr))


def test_bucket_sort_in_0_1_range():
    arr = [0.1, 0.9, 0.3, 0.7, 0.2, 0.8]
    assert sorted(bucket_sort(arr)) == sorted(arr)
    assert is_sorted(bucket_sort(arr))
    assert bucket_sort([]) == []
    assert bucket_sort([0.42]) == [0.42]
