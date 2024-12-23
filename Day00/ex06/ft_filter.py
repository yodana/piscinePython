def ft_filter(function, checklist):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""
    try:
        new_list = []
        if function is None:
            new_list = [l for l in checklist if bool(l) is not False]
            return new_list
        new_list = [l for l in checklist if function(l) is True]
        return new_list
    except TypeError as msg:
        print(msg)