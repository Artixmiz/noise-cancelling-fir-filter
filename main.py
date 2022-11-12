import sound
import filter
import numpy as np
import matplotlib.pyplot as plt

LEARNING_RATE = 0.01
NTAP = 100

count = 0

f = filter.Filter(np.zeros(NTAP))
y = np.empty(len(sound.LM3))

for i in range(len(sound.LM3)):
    count += 1
    if count == 10:
        ref_noise = sound.LN3[i]  # Reference noise
        est_noise = f.filter(ref_noise)  # Filter Operation ( Send reference noise to filter )
        error_signal = sound.LM3[i] - est_noise  # Noisy signal - Output of filter
        f.lms(error_signal, LEARNING_RATE)  # Update filter coefficients ( weight )

        print(est_noise, error_signal)

        y[i] = error_signal  # Output signal
        count = 0

length = y.shape[0] / 44100
time = np.linspace(0., length, y.shape[0])

fig, axs = plt.subplots(2)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
axs[0].plot(time, sound.LM3, label="Mixed Signal")
axs[1].plot(time, y, label="Estimated Signal")

plt.show()
