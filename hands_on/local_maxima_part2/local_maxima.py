def find_maxima(points):
    """Find local maxima of points.

    Input arguments:
    points -- 1D list of real numbers

    Output:
    indices -- list of indices of the local maxima in points
    """
    indices = []
    plateau_idx = []

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
            plateau_idx = []
        if points[i] == points[i+1]:
            plateau_idx.append(i)
        if points[i] > points[i+1] and plateau_idx:
            indices.append(plateau_idx[0])
            plateau_idx = []

    if points[-1] > points[-2]:
        indices.append(len(points)-1)
    return indices