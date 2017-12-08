from __future__ import division
import numpy as np
from .core import autocorrelation_1d

def msd(pos):
    """
    Compute the mean-squared displacement for a single particles using the
    Fast Correlation Algorithm.
    """

    pos = np.array(pos, copy=True)
    pos -= pos[0]
    N = len(pos)
    rsq = np.sum(pos**2, axis=1)
    MSD = np.zeros(N, dtype=float)

    SAB = autocorrelation_1d(pos[:,0])
    for i in range(1, pos.shape[1]):
        SAB += autocorrelation_1d(pos[:,i])

    SUMSQ = 2*np.sum(rsq)

    m = 0
    MSD[m] = SUMSQ - 2*SAB[m]*N

    for m in range(1, N):
        SUMSQ = SUMSQ - rsq[m-1] - rsq[N-m]
        MSD[m] = SUMSQ/(N-m) - 2*SAB[m]

    return MSD    
