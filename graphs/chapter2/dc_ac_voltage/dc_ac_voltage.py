import numpy as np
import matplotlib.ticker as tker
import matplotlib.pyplot as plt
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

x = np.linspace(0, 6 * np.pi, 1000)
ac = 5 * np.sin(x)
dc = 5 * np.ones_like(x)

plt.plot(x, ac)
plt.plot(x, dc)
plt.xticks([])
plt.yticks(np.linspace(-7, 7, 8))

plt.grid()
plt.margins(x=0.)


plt.xlabel('Time (t)')
plt.ylabel('Voltage (V)')
plt.savefig(os.path.join(dir_path, 'dc_ac_voltage.png'))
plt.show()

