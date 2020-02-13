import numpy as np
import tidynamics

def test_length_one_msd():
    N = 1
    pos = np.zeros(N)
    reference_msd = np.zeros(N)
    computed_msd = tidynamics.msd(pos)
    assert np.allclose(reference_msd, computed_msd)

def test_length_zero_msd():
    N = 0
    pos = np.zeros(N)
    reference_msd = np.zeros(N)
    computed_msd = tidynamics.msd(pos)
    assert np.allclose(reference_msd, computed_msd)

def test_length_one_msd_nd():
    N = 1
    ND = 4
    data = np.ones((N, ND))
    reference_msd = np.zeros_like(data[:,0])
    computed_msd = tidynamics.msd(data)
    assert np.allclose(reference_msd, computed_msd)
