def find_maxima(x_arr):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """

    local_maxs=[]
    for i,x in enumerate(x_arr):
        if i>=1 and i<len(x_arr)-1:
            if x>x_arr[i-1] and x>x_arr[i+1]:
                local_maxs.append(i)
    return local_maxs



x_arr=[1,3,-2,0,2,1]
x_arr=[4,2,1,3,1,5]
x_arr=[1,2,2,3,1]
print(find_maxima(x_arr))

# import numpy as np 
# x=x_arr
# print(np.diff(np.diff(x)))

# (p.diff(x)>0)

