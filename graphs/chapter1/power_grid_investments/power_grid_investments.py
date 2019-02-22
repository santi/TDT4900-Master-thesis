import numpy as np
import matplotlib.pyplot as plt
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

x = [*range(1997,2019)]
y = [4856, 5234, 5246, 4668, 5392,6215,7881,8931,8325,10248,11918,14442,12606,14612,16873,19178,20422,21677,23114,26222,31396,41737]

plt.plot(x, y)
plt.yticks([0, 10000, 20000, 30000, 40000])
plt.xticks([*range(1997,2019, 2)])

plt.grid()

plt.xlabel('Year')
plt.ylabel('Million NOK')
plt.savefig(os.path.join(dir_path, 'power_grid_investments.eps'), format='eps')
plt.show()

