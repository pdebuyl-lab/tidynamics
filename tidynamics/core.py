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

def correlation_1d(data1, data2):
    """
    Compute the correlation of two scalar time series.
    """

    N = len(data1)
    assert N == len(data2)

    # Pad the signal with zeros to avoid the periodic images.
    R_data1 = np.zeros(2*N)
    R_data1[:N] = data1
    R_data2 = np.zeros(2*N)
    R_data2[:N] = data2
    F_data1 = np.fft.fft(R_data1)
    F_data2 = np.fft.fft(R_data2)
    result = np.fft.ifft(F_data1.conj()*F_data2)
    positive_time = result[:N].real/(N-np.arange(N))
    negative_time = result[-N+1:][::-1].real/(N-1-np.arange(N-1))

    return np.concatenate((negative_time[::-1], positive_time))
