import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

samplerate, data = wavfile.read("Sound/Mixed-3_1.wav")
length = data.shape[0] / samplerate
print(samplerate)
print(len(data))
print(len(data) / samplerate)

time = np.linspace(0., length, data.shape[0])
plt.plot(time, data, label="Left channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
