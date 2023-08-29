from first import plus


def test_plus_int():
    value1 = 1
    value2 = 2
    expected = 3

    result = plus(value1,value2)

    assert result == expected

from math import isclose
def test_plus_float():
    value1 = 1.1
    value2 = 2.2
    expected = 3.3

    result = plus(value1,value2)

    assert isclose(expected,result)

import numpy as np
from numpy.testing import assert_allclose
def test_plus_arr():
    value1 = np.array([1,1])
    value2 = np.array([2,2])
    expected = np.array([3,3])

    result = plus(value1,value2)

    assert_allclose(expected,result)