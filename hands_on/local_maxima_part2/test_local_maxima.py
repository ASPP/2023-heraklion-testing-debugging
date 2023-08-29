from local_maxima import find_maxima
import numpy as np


def test_find_maxima():
    values = [1, 3, -2, 0, 2, 1]
    expected = [1, 4]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_edges():
    values = [4, 2, 1, 3, 1, 5]
    expected = [0, 3, 5]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_empty():
    values = []
    expected = []
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_plateau():
    values = [1, 2, 2, 1]
    expected_v1 = [1]
    expected_v2 = [2]
    expected_v3 = [1, 2]

    assert (np.all(find_maxima(values) == expected_v1) 
            or np.all(find_maxima(values) == expected_v2) 
            or np.all(find_maxima(values) == expected_v3))


def test_find_maxima_not_a_plateau():
    values = np.array([1, 2, 2, 3, 1])
    expected = np.array([3])

    assert np.all(find_maxima(values) == expected)
