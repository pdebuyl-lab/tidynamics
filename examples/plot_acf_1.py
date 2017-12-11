"""
========================
Autocorrelation function
========================

Generate the velocity for a Ornstein-Uhlenbeck process and compute its autocorrelation
function.
"""

import numpy as np
import tidynamics
import matplotlib.pyplot as plt

gamma = 2.7
T = 0.1
dt = 0.02
v_factor = np.sqrt(2*T*gamma*dt)

N = 32768
v = 0
for i in range(100):
    v = v - gamma*v*dt + v_factor*np.random.normal()
v_data = []
for i in range(N):
    v = v - gamma*v*dt + v_factor*np.random.normal()
    v_data.append(v)
v_data = np.array(v_data)

acf = tidynamics.acf(v_data)[:N//64]

time = np.arange(N//64)*dt

plt.plot(time, acf, label='VACF (num.)')

plt.plot(time, T*np.exp(-gamma*time), label='VACF (theo.)')

plt.legend()
plt.title('Examples for the VACF')
plt.show()
