import numpy as np


class Filter:
    def __init__(self, _coefficients, mu):
        self.ntaps = len(_coefficients)
        self.coefficients = _coefficients
        self.buffer = np.zeros(self.ntaps)
        self.mu = mu

    def filter(self, noise):  # Compute the output of the filter
        self.buffer[0] = noise
        return np.inner(self.coefficients, self.buffer)

    def lms(self, error):  # Update the coefficients of the filter
        for j in range(self.ntaps - 1, -1, -1):
            # Update coefficients
            self.coefficients[j] = self.coefficients[j] + self.mu * error * self.buffer[j]
            # Update buffer
            self.buffer[j] = self.buffer[j - 1]

    def nlms(self, error, beta=0.25):  # Update the coefficients of the filter
        self.mu = 0.00001  # 0.00001
        for j in range(self.ntaps - 1, -1, -1):
            # Update coefficients
            # self.coefficients[j] = self.coefficients[j] + self.mu / (
            #         gamma + np.dot(self.buffer[j], self.buffer[j])) * self.buffer[j] * error
            test = 1. / (np.dot(self.buffer[j], self.buffer[j]) + beta)
            self.coefficients[j] = self.coefficients[j] + self.mu * error * self.buffer[j] * test
            # Update buffer
            self.buffer[j] = self.buffer[j - 1]
