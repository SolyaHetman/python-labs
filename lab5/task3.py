import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance

def contrast():
    img = Image.open('photo.jpg')
    enhancer = ImageEnhance.Contrast(img)
    plt.imshow(enhancer.enhance(0.1))
    plt.show()
    plt.imshow(enhancer.enhance(100.0))
    plt.show()

def color_breaking():
    im = plt.imread('photo.jpg')
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    for c, ax in zip(range(3), axs):
        tmp_im = np.zeros(im.shape, dtype="uint8")
        tmp_im[:, :, c] = im[:, :, c]
        ax.imshow(tmp_im)
    plt.show()


def rgb2gray():
    rgb = plt.imread('photo.jpg')
    gray = np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
    plt.imshow(gray, cmap=plt.get_cmap('gray'))
    plt.show()

if __name__ == '__main__':
    im = plt.imread('photo.jpg')
    n = 1

    print(' 1 = rgb2gray'
          ' 2 = contrast'
          ' 3 = color breaking'
          ' 0 = to exit')
    while (n != 0):
        n = int(input())
        if (n == 1):
            rgb2gray()
        elif (n == 2):
            contrast()
        elif (n == 3):
            color_breaking()