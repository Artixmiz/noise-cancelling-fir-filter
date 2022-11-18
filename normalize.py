import numpy as np


class Main:
    def __init__(self):
        self.x_min = -0.5
        self.x_max = 0.5
        self.diff = 0
        self.diff_arr = 0

    def normalize(self, arr, x_min=-0.5, x_max=0.5):
        self.x_min = x_min
        self.x_max = x_max
        self.diff = self.x_max - self.x_min
        self.diff_arr = np.max(arr) - np.min(arr)
        return [(((i - min(arr)) * self.diff) / self.diff_arr) + self.x_min for i in arr]

    def denormalize(self, arr):
        return [(self.diff_arr * (i - self.x_min)) / self.diff + min(arr) for i in arr]


def new_normalize(x):
    temp = np.max(x) - np.min(x)
    x = x - np.min(x)  # x is in range [0;b-a]
    x = x / temp  # x is in range [0;1]
    x = x - 0.5  # x is in range [-0.5;0.5]
    x = x * 2  # x is in range [-1;1]

    return x
