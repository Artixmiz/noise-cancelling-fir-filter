from scipy.io import wavfile
import sound
import filter
import numpy as np
import matplotlib.pyplot as plt
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

# Configuration
INPUT_FILE = sound.LM2
KNOWN_NOISE = sound.LN2
STEP_SIZE = 0.00001  # 0.000000001 best for LMS, 0.00001 for NLMS
NTAP = 3

KNOWN_SIGNAL = sound.LS2


def main(desired, noise, mu, ntaps):
    st = time.time()
    f = filter.Filter(np.zeros(ntaps), mu)
    e = np.empty(len(desired))
    n_hat = np.empty(len(desired))

    if config["DEFAULT"]["coefficient"] == "":
        f.coefficients = np.zeros(ntaps)
    else:
        f.coefficients = np.array(config["DEFAULT"]["coefficient"])

    # Delay incase no known noise

    # noise = np.roll(desired, -6)

    for i in range(len(desired)):  # 2 minutes
        # n ---> filter ---> n_hat
        n_hat[i] = f.filter(noise[i])  # get estimate noise as output

        # e = d - y
        e[i] = desired[i] - n_hat[i]  # get error value, also serve as system output

        # adaptive algorithm
        f.nlms(e[i])

    with open("config.ini", "w") as configfile:
        # update config
        config["DEFAULT"]["coefficient"] = str(f.coefficients)
        config.write(configfile)

    et = time.time()

    plt.figure(1, figsize=(8, 4.5))
    plt.subplot(211)
    plt.grid(True)
    plt.title("Corrupted Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.ylim(-25000, 25000)
    plt.plot(INPUT_FILE, "tab:blue", alpha=0.9, label="Input", linewidth=0.3)
    plt.tight_layout()
    plt.subplot(212)
    plt.grid(True)
    plt.title("Output Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.ylim(-25000, 25000)
    plt.plot(INPUT_FILE, "tab:blue", alpha=0.25, label="Input", linewidth=0.3)
    plt.plot(e, "tab:orange", alpha=0.9, label="Input", linewidth=0.3)
    plt.tight_layout()

    plt.figure(2, figsize=(8, 4.5))
    plt.subplot(211)
    plt.grid(True)
    plt.title("Known Noise")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.ylim(-25000, 25000)
    plt.plot(KNOWN_NOISE, "tab:blue", alpha=0.9, label="Input", linewidth=0.3)
    plt.tight_layout()
    plt.subplot(212)
    plt.grid(True)
    plt.title("Estimated Noise")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.ylim(-25000, 25000)
    plt.plot(KNOWN_NOISE, "tab:blue", alpha=0.25, label="Input", linewidth=0.3)
    plt.plot(n_hat, "tab:orange", alpha=0.9, label="Input", linewidth=0.3)
    plt.tight_layout()

    # plt.figure(3, figure=(8, 4.5))
    # plt.grid(True)
    # plt.title("Test")
    # plt.xlabel("IDK")
    # plt.ylabel("I also don't know")


    wavfile.write("estimated_signal.wav", 44100, e.astype(np.int16))
    wavfile.write("estimated_noise.wav", 44100, np.invert(n_hat.astype(np.int16)))

    elapsed = et - st
    print("=====================================")
    print("Noise Correlation: ", np.corrcoef(n_hat, KNOWN_NOISE)[0, 1])
    print("Elapsed time: " + str(elapsed) + " seconds")
    print("=====================================")

    plt.show()


main(INPUT_FILE, KNOWN_NOISE, STEP_SIZE, NTAP)
