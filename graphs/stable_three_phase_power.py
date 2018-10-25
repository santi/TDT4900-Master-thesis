from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 2000)
s1 = np.sin(2.0 * np.pi * t)
s2 = np.sin(2.0 * np.pi * t + (2 * np.pi) / 3)
s3 = s1 + s2

"""
    Plot time dependent signal
"""

plt.ylabel("Amplitude")
plt.xlabel("Time [s]")

plt.xticks([0, 1./ 4, 1./ 4 + 1. / 3, 1./ 4 + 2. / 3], ['0', r'$\frac{1}{2} \pi$', r'$(\frac{1}{2} + \frac{2}{3}) \pi$', r'$(\frac{1}{2} + \frac{4}{3}) \pi$'])
plt.yticks([-1, -0.5, 0, 0.5, 1])

plt.margins(x=0., y=.1)
plt.grid()

plt.plot(t, s1, label='Phase 1')
plt.plot(t, s2, label='Phase 2')
plt.plot(t, s3, label='Stable signal')
plt.legend(loc=1)
plt.show()
