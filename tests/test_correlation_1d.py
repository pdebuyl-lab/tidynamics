import numpy as np
import tidynamics

def test_correlation_acf_1():
    N = 100
    data = np.random.random(size=N)
    acf = tidynamics.acf(data)
    comparison = tidynamics.core.correlation_1d(data, data)
    assert np.allclose(acf, comparison[-N:])

def test_cst_correlation_acf():
    N = 200
    x = 3.5
    data1 = np.ones(N)
    data2 = x*np.ones(N)
    reference_cf = x*np.ones(2*N-1)
    computed_cf = tidynamics.core.correlation_1d(data1, data2)
    assert np.allclose(reference_cf, computed_cf)
    
