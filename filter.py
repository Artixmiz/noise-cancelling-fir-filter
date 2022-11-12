import numpy as np


class Filter:
    def __init__(self, _coefficients):
        self.ntaps = len(_coefficients)
        self.coefficients = _coefficients
        self.buffer = np.zeros(self.ntaps)

    def filter(self, noise):  # Compute the output of the filter
        output = 0.
        self.buffer[0] = noise
        for j in range(self.ntaps):
            output += self.coefficients[j] * self.buffer[j]

        return output  # Return estimated noise

    def lms(self, error, mu=0.01):  # Update the coefficients of the filter
        for j in range(self.ntaps - 1, -1, -1):
            self.coefficients[j] += mu * error * self.buffer[j]  # Update coefficients
            self.buffer[j] = self.buffer[j - 1]  # Update buffer
