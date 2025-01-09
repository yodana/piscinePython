""" Filters of an image """

from matplotlib import pyplot as plt
import numpy as np


def ft_invert(array) -> list:
    """Inverse the color of an image"""
    ar = array.squeeze()
    print(array)
    new = [[255-ar[j][i] for i in range(len(ar[0]))] for j in range(len(ar))]
    try:
        plt.imshow(new)
        plt.axis("off")
        plt.show()
    except Exception as e:
        print("Something in plt went wrong:", e)
        return []
    return new


def ft_red(array) -> list:
    """ Filter red of an image """
    a = array.squeeze()
    n = [[[a[j][i][0], 0, 0] for i in range(len(a[0]))] for j in range(len(a))]
    try:
        plt.imshow(n)
        plt.axis("off")
        plt.show()
    except Exception as e:
        print("Something in plt went wrong:", e)
        return []
    return n


def ft_green(array) -> list:
    """ Filter green of an image """
    a = array.squeeze()
    n = [[[0, a[j][i][1], 0] for i in range(len(a[0]))] for j in range(len(a))]
    try:
        plt.imshow(n)
        plt.axis("off")
        plt.show()
    except Exception as e:
        print("Something in plt went wrong:", e)
        return []
    return n


def ft_blue(array) -> list:
    """ Filter blue of an image """
    a = array.squeeze()
    n = [[[0, 0, a[j][i][2]] for i in range(len(a[0]))] for j in range(len(a))]
    try:
        plt.imshow(n)
        plt.axis("off")
        plt.show()
    except Exception as e:
        print("Something in plt went wrong:", e)
        return []
    return n


def ft_grey(array) -> list:
    """ Filter grey of an image """
    array = array.squeeze()
    for i in range(len(array)):
        for j in range(len(array[0])):
            m = np.mean(array[i][j])
            array[i][j] = [m, m, m]
    try:
        plt.imshow(array)
        plt.axis("off")
        plt.show()
    except Exception as e:
        print("Something in plt went wrong:", e)
        return []
    return array
