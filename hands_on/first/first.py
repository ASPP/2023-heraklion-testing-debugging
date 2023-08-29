def times_3(x):
    """ Multiply x by 3.

    Parameters
    ----------
    x : The item to multiply by 3.
    """
    return x * 3

def plus(*args):
    """
    add values x and y
    """
    res=0
    for x in args:
        res+=x
    return res