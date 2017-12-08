import numpy as np
import tidynamics

def test_cst_acf():
    N = 100
    data = np.ones(N)
    reference_acf = np.ones_like(data)
    computed_acf = tidynamics.acf(data)
    assert np.allclose(reference_acf, computed_acf)
