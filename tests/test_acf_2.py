import numpy as np
import tidynamics

def test_cst_acf_1d():
    N = 0
    data = np.ones(N)
    reference_acf = np.ones_like(data)
    print(reference_acf)
    computed_acf = tidynamics.acf(data)
    assert np.allclose(reference_acf, computed_acf)

def test_cst_acf_nd():
    N = 0
    ND = 3
    data = np.ones((N, ND))
    reference_acf = ND*np.ones(N)
    computed_acf = tidynamics.acf(data)
    assert np.allclose(reference_acf, computed_acf)
