import numpy as np
import tidynamics

def test_random_walk_msd():

    def brute_force_msd(pos):
        """
        Compute the mean-square displacement with an explicit loop over all
        time intervals.
        """
        pos = np.asarray(pos)
        if pos.ndim==1:
            pos = pos.reshape((-1,1))
        trajectory_length = len(pos)
        msd = np.zeros(trajectory_length)
        msd_count = np.zeros(trajectory_length)
        for i in range(trajectory_length):
            for j in range(i, trajectory_length):
                msd[j-i] += np.sum((pos[i]-pos[j])**2)
                msd_count[j-i] += 1
        msd = msd/msd_count
        return msd

    N = 200
    N_dim = 2
    # Generate steps of value +/- 1
    steps = -1 + 2*np.random.randint(0, 2, size=(N, N_dim))
    # Compute random walk position
    walk = np.cumsum(steps, axis=0)

    tidynamics_msd = tidynamics.msd(walk)
    comparison_msd = brute_force_msd(walk)

    assert np.allclose(tidynamics_msd, comparison_msd)
