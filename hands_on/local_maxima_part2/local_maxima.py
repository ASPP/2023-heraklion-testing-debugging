import numpy as np

def find_maxima(x):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """
    local_maxima = []
    print('start')
    if len(x)>0:
        diff_values = np.diff(x)
        if np.any(diff_values==0):
            index_of_plateau = np.argwhere(diff_values==0)
            if x[int(index_of_plateau)] == np.max(x):
                local_maxima.append(int(index_of_plateau))
                return local_maxima
    for i in range(0, len(x)):
        if i==0:
            first_value = x[i]
            second_value = x[i+1]
            if first_value > second_value:
                local_maxima.append(i)
        elif i==len(x)-1:
            first_value = x[i-1]
            second_value = x[i]
            if first_value < second_value:
                local_maxima.append(i)
        else:
            first_value = x[i-1]
            second_value = x[i]
            third_value = x[i+1]
            if first_value < second_value and second_value > third_value:
                local_maxima.append(i)
    return local_maxima

