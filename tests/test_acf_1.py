import numpy as np
import tidynamics

def test_cst_acf_1d():
    N = 100
    data = np.ones(N)
    reference_acf = np.ones_like(data)
    computed_acf = tidynamics.acf(data)
    assert np.allclose(reference_acf, computed_acf)

def test_cst_acf_nd():
    N = 100
    ND = 3
    data = np.ones((N, ND))
    reference_acf = ND*np.ones(N)
    computed_acf = tidynamics.acf(data)
    assert np.allclose(reference_acf, computed_acf)
