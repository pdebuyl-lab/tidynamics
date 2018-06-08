"""
=================
Scaling behaviour
=================

Compute the autocorrelation for varying time series lengths.

The figure displays the timing and a :math:`N log N` scaling law, demonstrating
the claimed complexity.
"""

import numpy as np
import tidynamics
import matplotlib.pyplot as plt
import time

all_N = 64*2**np.arange(14)
max_direct_N = 32768
all_time = []
direct_time = []
n_runs = 5

for N in all_N:
    t = 0
    direct_t = 0
    for i in range(n_runs):
        data = np.random.random(size=N)
        t0 = time.time()
        acf = tidynamics.acf(data)
        t += time.time() - t0
        if N <= max_direct_N:
            t0 = time.time()
            acf = np.correlate(data, data, mode='full')
            direct_t += time.time() - t0

    all_time.append(t/n_runs)
    if N <= max_direct_N:
        direct_time.append(direct_t/n_runs)

plt.plot(all_N, all_time, label='actual compute time')
plt.plot(all_N, all_time[-1] * all_N*np.log(all_N) / (all_N[-1]*np.log(all_N[-1])), label=r'$N\log N$ scaling')
plt.plot(all_N[:len(direct_time)], direct_time, label='np.correlate compute time', ls='--')

plt.xlabel(r'$N$')
plt.ylabel('time')

plt.loglog()
plt.legend()

plt.show()
