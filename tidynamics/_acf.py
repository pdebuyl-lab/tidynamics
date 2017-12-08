import numpy as np
from .core import autocorrelation_1d

def acf(data):
    """
    Compute the autocorrelation of the data using the Fast Correlation
    Algorithm.
    """

    data = np.asarray(data)
    if data.ndim==1:
        return autocorrelation_1d(data)
    elif data.ndim>1:
        result = autocorrelation_1d(data[:,0])
        for j in range(1, data.shape[1]):
            result += autocorrelation_1d(data[:,j])
        return result
