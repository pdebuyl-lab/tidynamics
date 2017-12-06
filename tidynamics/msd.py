import numpy as np

import scipy.signal

def msd_with_scipy(pos):
    """
    Compute the mean-squared displacement for a single particles using the Fast Correlation
    Algorithm (Kneller et al 1995)
    """

    pos = np.array(pos, copy=True)
    pos -= pos[0]
    N = len(pos)
    rsq = np.sum(pos**2, axis=1)
    MSD = np.zeros(N)

    SAB = scipy.signal.fftconvolve(pos[:,0], pos[:,0][::-1])[N-1:]
    for i in range(1, pos.shape[1]):
        SAB += scipy.signal.fftconvolve(pos[:,i], pos[:,i][::-1])[N-1:]

    SUMSQ = 2*np.sum(rsq)

    m = 0
    MSD[m] = SUMSQ - 2*SAB[m]

    for m in range(1, N):
        SUMSQ = SUMSQ - rsq[m-1] - rsq[N-m]
        MSD[m] = (SUMSQ - 2*SAB[m])/(N-m)
        
    return MSD    

msd = msd_with_scipy
