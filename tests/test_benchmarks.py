from src.Benchmarks import timeit_once, benchmark_sorts
from src.sorts import bubble_sort, quick_sort


def test_timeit_once():
    def sort(a):
        return sorted(a)

    t = timeit_once(sort, [3, 1, 2])
    assert type(t) == float
    assert t >= 0.0


def test_benchmark_sorts():
    arrays = {
        "first": [3, 1, 2],
        "second": [10, -1, 5],
    }
    algos = {
        "bubble": bubble_sort,
        "quick": quick_sort,
    }

    result = benchmark_sorts(arrays, algos)

    assert set(result.keys()) == {"first", "second"}
    for name in arrays.keys():
        assert set(result[name].keys()) == {"bubble", "quick"}
        for value in result[name].values():
            assert type(value) == float
            assert value >= 0.0
