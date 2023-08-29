def find_maxima(x):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """
    local_maxima = []
    for i in range(1, len(x)-1):
        first_value = x[i-1]
        second_value = x[i]
        third_value = x[i+1]
        if first_value < second_value and second_value > third_value:
            local_maxima.append(i)
    return local_maxima

test_list = [1,3,-2,0,2,1]

print(find_maxima(test_list))
