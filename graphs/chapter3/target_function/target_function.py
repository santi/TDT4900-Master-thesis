import numpy as np
import matplotlib.pyplot as plt
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

x = np.linspace(1, 5, 5)
target_y = [1, 2, 3, 5, 3]
learned_y = [1, 1.5, 3.5, 5.5, 3]


plt.plot(x, target_y, 'ro', label='Data points')
plt.plot(x, target_y, label='Target function')
plt.plot(x, learned_y, label='Learned function')

plt.ylabel("Y")
plt.xlabel("X")
plt.legend()

fig = plt.gcf()
fig.set_size_inches(10,5)

plt.savefig(os.path.join(dir_path, 'target_function.eps'), format='eps')
plt.show()
