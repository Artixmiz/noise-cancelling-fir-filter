from scipy.io import wavfile

# Signal
SLS1, LS1 = wavfile.read("Sound/Signal-1_0.wav")
SRS1, RS1 = wavfile.read("Sound/Signal-1_1.wav")
SLS2, LS2 = wavfile.read("Sound/Signal-2_0.wav")
SRS2, RS2 = wavfile.read("Sound/Signal-2_1.wav")
SLS3, LS3 = wavfile.read("Sound/Signal-3_0.wav")
SRS3, RS3 = wavfile.read("Sound/Signal-3_1.wav")

# Noise
SLN1, LN1 = wavfile.read("Sound/Noise-1_0.wav")
SRN1, RN1 = wavfile.read("Sound/Noise-1_1.wav")
SLN2, LN2 = wavfile.read("Sound/Noise-2_0.wav")
SRN2, RN2 = wavfile.read("Sound/Noise-2_1.wav")
SLN3, LN3 = wavfile.read("Sound/Noise-3_0.wav")
SRN3, RN3 = wavfile.read("Sound/Noise-3_1.wav")

# Mixed (Signal + Noise)
SLM1, LM1 = wavfile.read("Sound/Mixed-1_0.wav")
SRM1, RM1 = wavfile.read("Sound/Mixed-1_1.wav")
SLM2, LM2 = wavfile.read("Sound/Mixed-2_0.wav")
SRM2, RM2 = wavfile.read("Sound/Mixed-2_1.wav")
SLM3, LM3 = wavfile.read("Sound/Mixed-3_0.wav")
SRM3, RM3 = wavfile.read("Sound/Mixed-3_1.wav")

# Combined
SLC1, LC1 = wavfile.read("Sound/Combine-1_0.wav")
SRC1, RC1 = wavfile.read("Sound/Combine-1_1.wav")
SLC2, LC2 = wavfile.read("Sound/Combine-2_0.wav")
SRC2, RC2 = wavfile.read("Sound/Combine-2_1.wav")
SLC3, LC3 = wavfile.read("Sound/Combine-3_0.wav")
SRC3, RC3 = wavfile.read("Sound/Combine-3_1.wav")
