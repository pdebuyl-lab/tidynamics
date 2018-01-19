from __future__ import division
import numpy as np
from .core import autocorrelation_1d
import itertools

def acf(data):
    """Autocorrelation of the input data using the Fast Correlation Algorithm.

    For D-dimensional time series, a sum is performed on the last dimension.

    Args:
        data (array-like): The input signal, of shape (N,) or (N,D).

    Returns:
        ndarray of shape (N,) with the autocorrelation for successive linearly
        spaced time delays

    """

    data = np.asarray(data)
    if data.ndim==1:
        return autocorrelation_1d(data)
    elif data.ndim>1:
        result = autocorrelation_1d(data[:,0])
        for j in range(1, data.shape[1]):
            result += autocorrelation_1d(data[:,j])
        return result

def msd(pos):
    """Mean-squared displacement (MSD) for single trajectories using the Fast
    Correlation Algorithm.

    Args:
        pos (array-like): The input trajectory, of shape (N,D).

    Returns:
        : ndarray of shape (N,) with the MSD for successive linearly spaced time
        delays.

    """

    pos = np.array(pos, copy=True, dtype=float)
    if pos.ndim==1:
        pos = pos.reshape((-1,1))
    N = len(pos)
    rsq = np.sum(pos**2, axis=1)
    MSD = np.zeros(N, dtype=float)

    SAB = autocorrelation_1d(pos[:,0])
    for i in range(1, pos.shape[1]):
        SAB += autocorrelation_1d(pos[:,i])

    SUMSQ = 2*np.sum(rsq)

    m = 0
    MSD[m] = SUMSQ - 2*SAB[m]*N

    MSD[1:] = (SUMSQ - np.cumsum(rsq)[:-1] - np.cumsum(rsq[1:][::-1])) / (N-1-np.arange(N-1))
    MSD[1:] -= 2*SAB[1:]

    return MSD

def cross_displacement(x):
    """Cross displacement of the components of x.

    Args:
        x (array-like): The input trajectory, of shape (N, D).

    Returns:
        : list of lists of times series, where the fist two indices [i][j]
        denote the coordinates for the cross displacement: "(Delta x[:,i]) (Delta x[:,j])".

    """

    x = np.array(x)
    if x.ndim != 2:
        raise ValueError("Incorrect input data for cross_displacement")
    D = x.shape[1]

    # Precompute the component-wise MSD
    split_msd = [msd(xi) for xi in x.T]

    # Create list of lists for the output
    result = [[] for i in range(D)]
    for i, j in itertools.product(range(D), range(D)):
        result[i].append([])

    for i, j in itertools.product(range(D), range(D)):
        if i==j:
            result[i][j] = split_msd[i]
        else:
            sum_of_x = msd(x[:,i]+x[:,j])
            result[i][j] = 0.5*(sum_of_x - split_msd[i] - split_msd[j])

    return result
