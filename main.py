import scipy.io.wavfile as wavfile
import sound
import filter
import numpy as np
import matplotlib.pyplot as plt
import time

# Configuration
INPUT_FILE = sound.LM2
KNOWN_NOISE = sound.LN2
STEP_SIZE = 0.000000001  # 0.000000001 best for LMS, 0.00001 for NLMS
NTAP = 1

KNOWN_SIGNAL = sound.LS2


def main(desired, noise, mu, ntaps):
    st = time.time()
    f = filter.Filter(np.zeros(ntaps), mu)
    e = np.empty(len(desired), dtype=np.float64)
    n_hat = np.empty(len(desired), dtype=np.float64)

    for i in range(len(desired)):  # 2 minutes
        # n ---> filter ---> n_hat
        n_hat[i] = f.filter(noise[i])  # get estimate noise as output

        # e = d - y
        e[i] = desired[i] - n_hat[i]  # get error value, also serve as system output

        # adaptive algorithm
        f.lms(e[i])

    et = time.time()

    plot_signals("Corrupted Signal", INPUT_FILE, "Output Signal", e)
    plot_signals("Known Noise", KNOWN_NOISE, "Estimated Noise", n_hat)

    wavfile.write("estimated_signal.wav", 44100, e.astype(np.int16))
    wavfile.write("estimated_noise.wav", 44100, np.invert(n_hat.astype(np.int16)))

    elapsed = et - st
    output = "Noise Correlation: {:.2f} \nElapsed time: {:.2f} seconds".format(np.corrcoef(n_hat, KNOWN_NOISE)[0, 1],
                                                                               elapsed)
    print("=====================================")
    print(output)
    print("=====================================")

    plt.show()


def plot_signals(title1, signal1, title2, signal2, y_lim=(-25000, 25000)):
    plt.figure(figsize=(8, 4.5))
    plt.subplot(211)
    plt.grid(True)
    plt.title(title1)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.ylim(*y_lim)
    plt.plot(signal1, "tab:blue", alpha=0.9, label="Input", linewidth=0.3)
    plt.tight_layout()
    plt.subplot(212)
    plt.grid(True)
    plt.title(title2)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.ylim(*y_lim)
    plt.plot(signal1, "tab:blue", alpha=0.25, label="Input", linewidth=0.3)
    plt.plot(signal2, "tab:orange", alpha=0.9, label="Input", linewidth=0.3)
    plt.tight_layout()


main(INPUT_FILE, KNOWN_NOISE, STEP_SIZE, NTAP)
