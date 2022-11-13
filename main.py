from scipy.io import wavfile
import sound
import filter
import numpy as np
import matplotlib.pyplot as plt

# Configuration
INPUT_FILE = sound.LM3
KNOWN_SIGNAL = sound.LS3
KNOWN_NOISE = sound.LN3
WEIGHT_RATE = 1
LEARNING_RATE = 0.00000000008
NTAP = 21

f = filter.Filter(np.zeros(NTAP))
y = np.empty(len(INPUT_FILE))

for i in range(0, len(INPUT_FILE)):
    ref_noise = KNOWN_NOISE[i]  # Reference noise
    est_noise = f.filter(ref_noise)  # Filter Operation ( Send reference noise to filter )
    error_signal = INPUT_FILE[i] - est_noise  # Noisy signal - Output of filter
    f.lms(error_signal, LEARNING_RATE, WEIGHT_RATE)  # Update filter coefficients ( weight )

    y[i] = error_signal  # Output signal

print(f.coefficients[-5])
print(f.coefficients[-4])
print(f.coefficients[-3])
print(f.coefficients[-2])
print(f.coefficients[-1])

length = y.shape[0] / 44100
time = np.linspace(0., length, y.shape[0])

# fig, axs = plt.subplots(2, 2)
# axs[0, 0].plot(time, sound.LS3)
# axs[0, 0].set_title("Signal")
#
# axs[1, 0].plot(time, sound.LN3)
# axs[1, 0].set_title("Noise")
# axs[1, 0].sharex(axs[0, 0])
#
# axs[0, 1].plot(time, sound.LM3)
# axs[0, 1].set_title("Mixed")
#
# axs[1, 1].plot(time, y)
# axs[1, 1].set_title("Estimated")
# axs[1, 1].sharex(axs[0, 1])
# fig.tight_layout()

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Correlation: ' + str(np.correlate(KNOWN_SIGNAL, y)))
ax1.plot(time, KNOWN_SIGNAL)
ax2.plot(time, INPUT_FILE)
ax3.plot(time, y)

plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

wavfile.write("output.wav", 44100, y.astype(np.int16))

plt.show()
