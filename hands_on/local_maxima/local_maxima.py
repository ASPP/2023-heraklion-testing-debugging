def find_maxima(x):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """
    local_max = []
    diffs = [f-i for i,f in zip(v[0:-1],v[1:])]
    for i in range(len(diffs)-1):
        if diffs[i] > 0 and diffs[i+1] < 0:
            local_max.append(i+1)
    return local_max