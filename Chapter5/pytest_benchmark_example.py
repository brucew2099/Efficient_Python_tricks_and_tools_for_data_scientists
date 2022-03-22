def list_comprehension(len_list=5):
    return list(range(len_list))


def test_concat(benchmark):
    res = benchmark(list_comprehension)
    assert res == [0, 1, 2, 3, 4]