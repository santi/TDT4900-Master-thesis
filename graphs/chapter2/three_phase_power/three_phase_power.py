import numpy as np
import matplotlib.pyplot as plt
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

t = np.linspace(0, 1, 2000)
s1 = np.sin(2.0 * np.pi * t)
s2 = np.sin(2.0 * np.pi * t + (2 * np.pi) / 3)
s3 = np.sin(2.0 * np.pi * t + (4 * np.pi) / 3)


plt.plot(t, s1, label='Phase 1')
plt.plot(t, s2, label='Phase 2')
plt.plot(t, s3, label='Phase 3')

plt.ylabel("Amplitude")
plt.xlabel("Time (s)")
plt.xticks([0, 1./ 4, 1./ 4 + 1. / 3, 1./ 4 + 2. / 3], ['0', r'$\frac{1}{2} \pi$', r'$(\frac{1}{2} + \frac{2}{3}) \pi$', r'$(\frac{1}{2} + \frac{4}{3}) \pi$'])
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.legend(loc=3)

plt.margins(x=0., y=.1)
plt.grid()

plt.savefig(os.path.join(dir_path, 'three_phase_power.png'))
plt.show()
