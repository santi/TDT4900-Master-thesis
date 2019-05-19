from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


TWO_PI = 2 * np.pi


def signal(t):
    return np.sin(t * TWO_PI) * 0.95 + np.sin(t * TWO_PI * 10) * 0.05


"""
    Low sampling frequency
"""

t1_viz = np.linspace(0, 1, 21)
s1_viz = signal(t1_viz)
t1 = np.linspace(0, 1, 20, endpoint=False)
s1 = signal(t1)

low_freq_signal = plt.figure(1)

plt.ylabel("Amplitude")
plt.xlabel("Time (t)")

plt.xticks([0, 0.5, 1], [r"$0$", r"$\frac{1}{2} π$", r"$π$"])
plt.yticks([])

plt.title("Low frequency sampling")
plt.plot(t1_viz, s1_viz)
plt.savefig(os.path.join(dir_path, "low_sampling_frequency_signal.eps"), format="eps")
low_freq_signal.show()


"""
    Low sampling frequency
"""


t2 = np.linspace(0, 1, 2000, endpoint=False)
s2 = signal(t2)

high_freq_signal = plt.figure(2)

plt.ylabel("Amplitude")
plt.xlabel("Time (t)")

plt.xticks([0, 0.5, 1], [r"$0$", r"$\frac{1}{2} π$", r"$π$"])
plt.yticks([])

plt.title("High frequency sampling")
plt.plot(t2, s2)
plt.savefig(os.path.join(dir_path, "high_sampling_frequency_signal.eps"), format="eps")
high_freq_signal.show()


"""
    Plot low-res frequencies
"""

low_frequencies = plt.figure(3)
fft = np.fft.fft(s1)
T = t1[1] - t1[0]  # sample rate
N = s1.size

f = np.linspace(0, 2 / T, N)
print(len(f))
print(len(fft))

plt.ylabel("Fourier coefficient")
plt.xlabel("Frequency (Hz)")
plt.bar(f[:15], np.abs(fft)[:15] * 2 / N)  # 2 / N is a normalization factor
plt.xticks(
    [*range(0, 30, 2)],
    [
        "0",
        "1π",
        "2π",
        "3π",
        "4π",
        "5π",
        "6π",
        "7π",
        "8π",
        "9π",
        "10π",
        "11π",
        "12π",
        "13π",
        "14π",
        # "15π",
        # "16π",
        # "17π",
        # "18π",
        # "19π",
    ],
)
# plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.savefig(os.path.join(dir_path, "low_sampling_frequency_fourier.eps"), format="eps")
low_frequencies.show()


"""
    Plot high-res frequencies
"""

high_frequencies = plt.figure(4)
fft2 = np.fft.fft(s2)
T2 = t2[1] - t2[0]  # sample rate
N2 = s2.size

f2 = np.linspace(0, 2 / T2, N2)
# print(len(f))
# print(len(fft))

plt.ylabel("Fourier coefficient")
plt.xlabel("Frequency (Hz)")
print(f2[:20])
plt.bar(f2[:15], np.abs(fft2)[:15] * 2 / N2)  # 2 / N is a normalization factor
plt.xticks(
    [*range(0, 30, 2)],
    [
        "0",
        "1π",
        "2π",
        "3π",
        "4π",
        "5π",
        "6π",
        "7π",
        "8π",
        "9π",
        "10π",
        "11π",
        "12π",
        "13π",
        "14π",
        # "15π",
        # "16π",
        # "17π",
        # "18π",
        # "19π",
    ],
)
# plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.savefig(os.path.join(dir_path, "high_sampling_frequency_fourier.eps"), format="eps")
plt.show()
