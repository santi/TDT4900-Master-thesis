from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

t = np.linspace(0, 2, 2000)
s = np.sin(2.0 * np.pi * t) + 0.5 * np.sin(2 * 2.0 * np.pi * t) + 0.2 * np.sin(4 * 2.0 * np.pi * t)
fft = np.fft.fft(s)
N = s.size


def add_labels():
    plt.ylabel("Amplitude")
    plt.xlabel("Time (t)")
    plt.xticks([0, 0.5, 1, 1.5, 2], ['0', '1π', '2π', '3π', '4π'])
    plt.yticks([x/10. for x in range(-12, 13, 2) ])



"""
    Plot all compositions
"""
all_compositions = plt.figure(1)
add_labels()

s1 = (np.abs(fft)[2] * 2 / N) * np.sin(2 * np.pi * t)
s2 = (np.abs(fft)[4] * 2 / N) * np.sin(4 * np.pi * t)
s3 = (np.abs(fft)[8] * 2 / N) * np.sin(8 * np.pi * t)

plt.plot(t, s1, label='1st component')
plt.plot(t, s2, label='2nd component')
plt.plot(t, s3, label='3rd component')
plt.legend()
plt.savefig(os.path.join(dir_path, 'fourier_analysis_comp_all.eps'), format='eps')
all_compositions.show()


"""
    Plot composition 1
"""

composition1 = plt.figure(2)
add_labels()

plt.plot(t, s1)
plt.savefig(os.path.join(dir_path, 'fourier_analysis_comp_1.eps'), format='eps')

composition1.show()



"""
    Plot composition 2
"""

composition2 = plt.figure(3)
add_labels()

plt.plot(t, s1 + s2)
plt.savefig(os.path.join(dir_path, 'fourier_analysis_comp_2.eps'), format='eps')

composition2.show()


"""
    Plot composition 3
"""

composition3 = plt.figure(4)
add_labels()

plt.plot(t, s1 + s2 + s3)
plt.savefig(os.path.join(dir_path, 'fourier_analysis_comp_3.eps'), format='eps')

plt.show()

