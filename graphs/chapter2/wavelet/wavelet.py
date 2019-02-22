
import numpy as np
import matplotlib.pyplot as plt
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def ricker_wavelet(f, length=0.512, dt=0.001):
    t = np.linspace(-length/2, (length-dt)/2, length/dt)
    y = (1.-2.*(np.pi**2)*(f**2)*(t**2))*np.exp(-(np.pi**2)*(f**2)*(t**2))
    return t, y

f = 5
t, y = ricker_wavelet(f)
plt.plot(t, y)

plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.savefig(os.path.join(dir_path, 'wavelet.eps'), format='eps')
plt.show()