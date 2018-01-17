import numpy as np
import tidynamics

def test_cross_disp_1():
    N = 100
    D = 4
    data = np.random.random(size=(N, D))
    cross_disp = tidynamics.cross_displacement(data)
    for i in range(D):
        assert np.allclose(cross_disp[i][i], tidynamics.msd(data[:,i]))
