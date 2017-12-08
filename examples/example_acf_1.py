import numpy as np
import tidynamics
import matplotlib.pyplot as plt

gamma = 2.7
T = 0.1
dt = 0.02
v_factor = np.sqrt(2*T*gamma*dt)

N = 3000
mean = np.zeros(N)
count = 0
for i in range(32):
    v = 0
    for i in range(100):
        v = v - gamma*v*dt + v_factor*np.random.normal()
    v_data = []
    for i in range(N):
        v = v - gamma*v*dt + v_factor*np.random.normal()
        v_data.append(v)
    v_data = np.array(v_data)
    mean += tidynamics.acf(v_data)
    count += 1

mean /= count
mean = mean[:N//4]

time = np.arange(N//4)*dt

plt.plot(time, mean, label='VACF (num.)')

plt.plot(time, T*np.exp(-gamma*time), label='VACF (theo.)')

plt.legend()
plt.title('Examples for the VACF')
plt.show()
