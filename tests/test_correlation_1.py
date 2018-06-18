import numpy as np
import tidynamics

def test_correlation_acf_1():
    N = 100
    size = (N, 4)
    data = np.random.random(size=size)
    acf = tidynamics.acf(data)
    comparison = tidynamics.correlation(data, data)
    assert np.allclose(acf, comparison[-N:])

def test_cst_correlation_acf():
    N = 200
    size = (N, 3)
    x = 3.5
    data1 = np.ones(shape=size)
    data2 = x*np.ones(shape=size)
    reference_cf = x*size[1]*np.ones(2*N-1)
    computed_cf = tidynamics.correlation(data1, data2)
    assert np.allclose(reference_cf, computed_cf)

