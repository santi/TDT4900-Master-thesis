from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 2000)
s = np.sin(2.0 * np.pi * t) + 0.5 * np.sin(2 * 2.0 * np.pi * t) + 0.2 * np.sin(4 * 2.0 * np.pi * t)

"""
    Plot time dependent signal
"""

plt.ylabel("Amplitude")
plt.xlabel("Time [s]")

plt.xticks([0, 0.5, 1, 1.5, 2], ['0', '1π', '2π', '3π', '4π'])
plt.yticks([x/10. for x in range(-12, 13, 2) ])

time_signal = plt.figure(1)
plt.plot(t, s)
time_signal.show()


"""
    Plot frequencies
"""
frequencies = plt.figure(2)
fft = np.fft.fft(s)
T = t[1] - t[0]  # sample rate
N = s.size

f = np.linspace(0, 2 / T, N)

plt.ylabel("Fourier coefficient")
plt.xlabel("Frequency [Hz]")
plt.bar(f[:10], np.abs(fft)[:10] * 2 / N, width=.2)  # 2 / N is a normalization factor
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ['0', '1π', '2π', '3π', '4π', '5π', '6π', '7π', '8π', '9π'])
plt.yticks([0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0])
frequencies.show()

input()
