from __future__ import division
import numpy as np

def autocorrelation_1d(data):
    """
    Compute the autocorrelation of a scalar time series.
    """

    N = len(data)

    # Pad the signal with zeros to avoid the periodic images.
    R_data = np.zeros(2*N)
    R_data[:N] = data
    F_data = np.fft.fft(R_data)
    result = np.fft.ifft(F_data*F_data.conj())[:N].real/(N-np.arange(N))

    return result
