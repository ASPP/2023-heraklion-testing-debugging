from plus import plus
import numpy as np
from math import isclose

def test_plus_123():
    x = 1
    y = 2
    assert plus(x,y) == 3

def test_plus_1dec1_2dec2_3dec3():
    x = 1.1
    y = 2.2
    assert isclose(plus(x,y), 3.3)

def test_plus_with_numpy():
    x = np.array([[1,1],[1,1]])
    y = np.array([[2,2],[2,2]])
    np.testing.assert_equal(plus(x,y), np.array([[3,3],[3,1]]))