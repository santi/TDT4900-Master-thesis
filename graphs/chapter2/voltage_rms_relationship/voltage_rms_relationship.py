
import numpy as np
import matplotlib.pyplot as plt
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Number of sample points
N = 1000
# sample spacing
T = 1.0 / N
x = np.linspace(0.0, 2 * np.pi, N)
y = np.sin(x)
rms = np.full_like(x, 1/np.sqrt(2))

plt.plot(x/np.pi, y, label=r'$V_{AC}$')
plt.plot(x/np.pi, rms, label=r'$V_{RMS}$')
plt.legend()

plt.xticks([0, 1, 2], ['0', 'π', '2π'])
plt.yticks([-1, 0, 1 / np.sqrt(2),1], ['-1', '0', r'$\frac{1}{\sqrt{2}}$','1'])
plt.gca().yaxis.grid(True)
plt.margins(0, 0.05)

plt.xlabel('Time (t)')
plt.ylabel('Voltage (V)')
plt.savefig(os.path.join(dir_path, 'voltage_rms_relationship.eps'), format='eps')
plt.show()