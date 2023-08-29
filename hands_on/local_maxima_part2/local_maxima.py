import numpy as np

def find_maxima(x: np.array):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """
    idx = []
    for i in range(0, len(x)):
        pred = True
        if i != 0:
            pred = pred and (x[i-1] <= x[i])
        if i != len(x)-1:
            pred = pred and (x[i+1] < x[i])
        if pred:
            idx.append(i)
    return idx


