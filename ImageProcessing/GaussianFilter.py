"""
Gaussian Filter is used in reducing noise in the image and also the details of the image.
https://medium.com/@akumar5/computer-vision-gaussian-filter-from-scratch-b485837b6e09
"""
import numpy as np

__author__ = 'roeiherz'


def convolution(oldimage, kernel):
    image_h = oldimage.shape[0]
    image_w = oldimage.shape[1]
    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]

    h = kernel_h // 2
    w = kernel_w // 2

    # image_pad = np.pad(oldimage, pad_width=((kernel_h // 2, kernel_h // 2), (kernel_w // 2, kernel_w // 2), (0, 0)),
    #                    mode='constant', constant_values=0).astype(np.float32)
    image_conv = np.zeros(oldimage.shape)

    for i in range(h, image_h - h):
        for j in range(w, image_w - w):
            x = oldimage[i - h: i + h, j - w:j + w]
            x = x.flatten() * kernel.flatten()
            image_conv[i, j] = x.sum()

    return image_conv[h:-h, w:-w]


def GaussianBlurImage(image, sigma):
    filter_size = 2 * int(4 * sigma + 0.5) + 1
    gaussian_filter = np.zeros((filter_size, filter_size), np.float32)
    m = filter_size // 2
    n = filter_size // 2

    for i in range(-m, m):
        for j in range(-n, n):
            x1 = 2 * np.pi * sigma ** 2
            x2 = (i ** 2 + j ** 2) / 2 * sigma ** 2
            gaussian_filter[i + m, j + n] = x2 / x1

    im_filtered = np.zeros_like(image, dtype=np.float32)
    for c in range(3):
        im_filtered[:, :, c] = convolution(image[:, :, c], gaussian_filter)

    return im_filtered
