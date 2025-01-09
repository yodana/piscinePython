""" Functions for loading a image """

import numpy as np
from PIL import Image


def ft_load(path: str) -> list:
    """ ft_load(path: str) -> list
    Function who loads an image, print the shape and
    his pixels contents in RGB format
    return the list of the pixels of the image in RGB format
    """

    try:
        msg_error = "AssertationError: "
        assert isinstance(path, str), \
            msg_error + "the path is not str type"
    except AssertionError as msg:
        print(msg)
        return []
    try:
        image = Image.open(path)
        assert image.format in ["JPEG", "JPG"], \
            "AssertionError: the format is not jpeg or jpg"
    except FileNotFoundError:
        print("The file was not found")
        return []
    except AssertionError as msg:
        print(msg)
        return []
    img_arr = np.array(image)
    print("The shape of the image is:", img_arr.shape)
    return img_arr
