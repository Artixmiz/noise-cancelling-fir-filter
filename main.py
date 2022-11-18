from scipy.io import wavfile
from scipy import fftpack
from sklearn.preprocessing import minmax_scale
import sound
import filter
import normalize
import numpy as np
import matplotlib.pyplot as plt
import time

# Configuration
INPUT_FILE = sound.LC3
KNOWN_NOISE = sound.LN3
LEARNING_RATE = 0.000000001
NTAP = 1

KNOWN_SIGNAL = sound.LS3


def main(desired, noise, mu, ntaps):
    st = time.time()
    f = filter.Filter(np.zeros(ntaps), mu)
    e = np.empty(len(desired))
    n_hat = np.empty(len(desired))

    # shifting stuff
    # A = fftpack.fft(desired)
    # B = fftpack.fft(noise)
    # Br = -B.conjugate()
    # shifting = np.argmax(np.abs(fftpack.ifft(A * Br)))
    # noise = np.roll(noise, shifting)

    # print(shifting)
    print(desired)
    print(noise)

    # normalize stuff
    # normalized_noise = (minmax_scale(noise) - 0.5) * 2
    # normalized_desired = (minmax_scale(desired) - 0.5) * 2
    #
    # print(normalized_noise)
    # print(normalized_desired)
    #
    # AMP = desired[0] / normalized_desired[0]

    for i in range(len(INPUT_FILE)):
        # n ---> filter ---> n_hat
        n_hat[i] = f.filter(noise[i])  # get estimate noise as output

        # e = d - y
        e[i] = desired[i] - n_hat[i]  # get error value, also serve as system output

        # adaptive algorithm
        f.lms(e[i])

    # print(e)
    # e *= AMP
    # print(e)

    et = time.time()

    length = e.shape[0] / 44100
    t = np.linspace(0., length, e.shape[0])

    # plt.figure(1)
    # plt.title("Estimated Signal")
    # plt.plot(INPUT_FILE, "r", alpha=0.3, label="Input", linewidth=0.3)
    # plt.plot(e, "b", alpha=1, label="Output", linewidth=0.3)
    # plt.tight_layout()
    #
    # plt.figure(2)
    # plt.title("GOAL")
    # plt.plot(INPUT_FILE, "r", alpha=0.3, label="Input", linewidth=0.3)
    # plt.plot(KNOWN_SIGNAL, "b", alpha=1, label="Output", linewidth=0.3)

    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
    fig.set_size_inches(17.5, 9.5)

    ax0.grid(True)
    ax0.set_title("Corrupted Signal")
    ax0.xaxis.set_label_text("Time (s)")
    ax0.yaxis.set_label_text("Amplitude")
    ax0.set_ylim(-20000, 20000)
    ax0.plot(t, INPUT_FILE, "m", alpha=0.9, label="Input", linewidth=0.3)

    ax1.grid(True)
    ax1.set_title("Estimated Signal")
    ax1.xaxis.set_label_text("Time (s)")
    ax1.yaxis.set_label_text("Amplitude")
    ax1.set_ylim(-20000, 20000)
    ax1.plot(t, INPUT_FILE, "m", alpha=0.3, label="Input", linewidth=0.3)
    ax1.plot(t, e, "b", alpha=0.9, label="Output", linewidth=0.3)

    ax2.grid(True)
    ax2.set_title("I don't know")
    ax2.xaxis.set_label_text("Frequency (Hz)")
    ax2.yaxis.set_label_text("Amplitude")
    ax2.plot(np.abs(np.fft.rfft(INPUT_FILE)), "c", alpha=0.3, label="Input", linewidth=0.9)

    wavfile.write("estimated_signal.wav", 44100, e.astype(np.int16))
    # wavfile.write("estimated_noise.wav", 44100, np.invert(n.astype(np.int16)))

    elapsed = et - st
    print("=====================================")
    print("Correlation: ", np.corrcoef(e, KNOWN_SIGNAL)[0, 1])
    print("Elapsed time: " + str(elapsed) + " seconds")
    print("=====================================")

    fig.tight_layout()
    plt.show()


main(INPUT_FILE, KNOWN_NOISE, LEARNING_RATE, NTAP)
