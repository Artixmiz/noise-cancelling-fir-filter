from scipy import fftpack
import sound
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 1])


print(a)
print(b)


A = fftpack.fft(a)
B = fftpack.fft(b)

Ar = -A.conjugate()
Br = -B.conjugate()

# shifting = np.argmax(np.abs(fftpack.ifft(A * Br)))
shifting = -3
n = np.roll(b, shifting)

# print(np.argmax(np.abs(fftpack.ifft(Ar * B))))
# print(np.argmax(np.abs(fftpack.ifft(A * Br))))

print(a)
print(n)
