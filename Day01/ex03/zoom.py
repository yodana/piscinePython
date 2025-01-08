""" This program zoom the image animal.jpeg """

from load_image import ft_load
from matplotlib import pyplot as plt


def main():
    """ Function main who contains the zoom and handle the errors """
    img = ft_load("animal.jpeg")
    if len(img) != 0:
        imgz = img[300:700, 300:700, :1]
        print("New shape after slicing: ", imgz.shape, end="")
        print(" or", img[300:700, 300:700, 0].shape)
        print(imgz)
        try:
            plt.imshow(imgz, cmap='gray')
            plt.savefig('animal_zoom.jpeg')
        except Exception as e:
            print("Something in plt went wrong:", e)


if __name__ == "__main__":
    main()
