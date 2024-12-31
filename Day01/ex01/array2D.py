""" function for calculate and manipulate an array2D """

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """ slice_me(family: list, start: int, end: int) -> list
    cut an array list depanding on the start and end index provided """
    try:
        msg_error = "AssertationError: "
        assert isinstance(start, int), \
            msg_error + "start value is not int type"
        assert isinstance(end, int), \
            msg_error + "end value is not int type"
        assert isinstance(family, list), \
            msg_error + "family value is not list type"
    except AssertionError as msg:
        print(msg)
        return []
    try:
        arr = np.array(family)
    except ValueError:
        print("All list in family list are not the same size")
        return []
    print("My shape is :", arr.shape)
    new_family = family[start:end]
    arr = np.array(new_family)
    print("My new shape is :", arr.shape)
    return new_family
