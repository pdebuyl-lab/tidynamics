import numpy as np
import tidynamics

def test_linear_msd():
    N = 100
    time = np.arange(N)
    reference_msd = time**2
    computed_msd = tidynamics.msd(time)
    assert np.allclose(reference_msd, computed_msd)

def test_cst_msd():
    N = 100
    data = np.ones(N)
    reference_msd = np.zeros_like(data)
    computed_msd = tidynamics.msd(data)
    assert np.allclose(reference_msd, computed_msd)
