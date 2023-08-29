def find_maxima(points):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """
    indices = []
    
    if not points:
        print("No input given")
        return []
    elif len(points) == 1:
        return [0]

    if points[0] > points[1]:
        indices.append(0)
    for i in range(1, len(points)-1):
        if points[i] > points[i+1] and points[i] > points[i-1]:
            indices.append(i)
    if points[-1] > points[-2]:
        indices.append(len(points)-1)
    return indices