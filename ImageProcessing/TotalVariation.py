"""
Computes the total variation norm and its gradient. From jcjohnson/cnn-vis.
https://gist.github.com/crowsonkb/ddf8167359be4ba2aa34835aa207e241
"""

import numpy as np

__author__ = 'roeiherz'


def tv_norm(x):
    x_diff = x - np.roll(x, -1, axis=1)
    y_diff = x - np.roll(x, -1, axis=0)
    grad_norm = x_diff ** 2 + y_diff ** 2 + 1e-6
    norm = np.sum(np.sqrt(grad_norm))

    dgrad_norm = 0.5 / np.sqrt(grad_norm)
    dx_diff = 2 * dgrad_norm * x_diff
    dy_diff = 2 * dgrad_norm * y_diff
    grad = dx_diff + dy_diff

    grad[:, 1:, :] -= dx_diff[:, :-1, :]
    grad[1:, :, :] -= dy_diff[:-1, :, :]
    return grad
