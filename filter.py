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

        # Return estimated noise
        return output

    def lms(self, error, mu=0.000000001, a=1):  # Update the coefficients of the filter
        for j in range(self.ntaps - 1, -1, -1):
            # Update coefficients
            self.coefficients[j] = a * self.coefficients[j] + mu * error * self.buffer[j]
            # Update buffer
            self.buffer[j] = self.buffer[j - 1]
