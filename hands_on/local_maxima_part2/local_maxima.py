def find_maxima(x_arr):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """

    local_maxs=[]
    for i,x in enumerate(x_arr):
        if i == 0 and x>x_arr[i+1]:
            local_maxs.append(i)
        elif i == len(x_arr)-1 and x>x_arr[i-1]:
            local_maxs.append(i)
        elif i>=1 and i<len(x_arr)-1:
            if x>x_arr[i-1] and x>x_arr[i+1]:
                local_maxs.append(i)
    return local_maxs