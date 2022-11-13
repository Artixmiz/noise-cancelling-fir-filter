from scipy.io import wavfile
from scipy.fftpack import fft
import sound
import filter
import numpy as np
import matplotlib.pyplot as plt
import time

st = time.time()

# Configuration
INPUT_FILE = sound.LM2
KNOWN_SIGNAL = sound.LS2
KNOWN_NOISE = sound.LN2
WEIGHT_RATE = 1
LEARNING_RATE = 0.00000000008
NTAP = 21

f = filter.Filter(np.zeros(NTAP))
y = np.empty(len(INPUT_FILE))
e = np.empty(len(INPUT_FILE))

count = 2

for i in range(len(INPUT_FILE)):
    if count == 2:
        e[i] = f.filter(KNOWN_NOISE[i])
        y[i] = INPUT_FILE[i] - e[i]
        f.lms(y[i], LEARNING_RATE, WEIGHT_RATE)
        count = 0

    count += 1

print(f.coefficients[-1])
print("=====================================")

length = y.shape[0] / 44100
x = np.linspace(0., length, y.shape[0])

n = np.size(x)
fr = 22050 * np.linspace(0, 1, n // 2)

# plot 1:
plt.subplot(4, 2, 1)
plt.title("Signal")
plt.ylabel("Amplitude")
plt.plot(x, sound.LS3)

# plot 3:
plt.subplot(4, 2, 3)
plt.title("Noise")
plt.ylabel("Amplitude")
plt.plot(x, sound.LN3)

# plot 5:
plt.subplot(4, 2, 5)
plt.title("Mixed")
plt.ylabel("Amplitude")
plt.plot(x, sound.LM3)

# plot 7:
plt.subplot(4, 2, 7)
plt.title("Output")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.plot(x, y)

# plot 2:
X = fft(sound.LS3)
X_mag = (2 / n) * np.abs(X[0:np.size(fr)])

plt.subplot(4, 2, 2)
plt.title("Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.plot(fr, X_mag)

# plot 4:
X = fft(sound.LN3)
X_mag = (2 / n) * np.abs(X[0:np.size(fr)])

plt.subplot(4, 2, 4)
plt.title("Noise")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.plot(fr, X_mag)

# plot 6:
X = fft(sound.LM3)
X_mag = (2 / n) * np.abs(X[0:np.size(fr)])

plt.subplot(4, 2, 6)
plt.title("Mixed")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.plot(fr, X_mag)

# plot 8:
X = fft(y)
X_mag = (2 / n) * np.abs(X[0:np.size(fr)])

plt.subplot(4, 2, 8)
plt.title("Output")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.plot(fr, X_mag)

plt.suptitle("Correlation: " + str(np.correlate(KNOWN_SIGNAL, y)))

# fig, (ax1, ax2, ax3) = plt.subplots(3)
# fig.suptitle('Correlation: ' + str(np.correlate(KNOWN_SIGNAL, y)))
# ax1.plot(x, KNOWN_SIGNAL)
# ax2.plot(x, INPUT_FILE)
# ax3.plot(x, y)
#
# plt.xlabel("Time [s]")
# plt.ylabel("Amplitude")

wavfile.write("estimated_signal.wav", 44100, y.astype(np.int16))
wavfile.write("estimated_noise.wav", 44100, np.invert(e.astype(np.int16)))

et = time.time()
elapsed = et - st
print("Elapsed time: " + str(elapsed) + " seconds")

plt.show()
