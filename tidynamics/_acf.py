import numpy as np
from .core import autocorrelation_1d

def acf(data):
    """
    Compute the autocorrelation of the data using the Fast Correlation
    Algorithm.
    """

    return autocorrelation_1d(data)
