Data format
===========

tidynamics assumes that the data is provided as NumPy arrays where the first index indicates
the timestep and the second index, if it exists, indicates in the spatial coordinates of the
trajectory. Data is assumed to be sampled at equal time intervals.

For a 2D position dataset ``pos``, :math:`x(t)` is stored in ``pos[:,0]`` and :math:`y(t)`
is stored in ``pos[:,1]``, as we show in the example below:

+---------------+------------+-----------+
| Index i       | pos[i,0]   | pos[i,1]  |
+===============+============+===========+
|   0           | x(0)       | y(0)      |
+---------------+------------+-----------+
|   1           | x(1)       | y(1)      |
+---------------+------------+-----------+
|   2           | x(2)       | y(2)      |
+---------------+------------+-----------+
| ...           | ...        | ...       |
+---------------+------------+-----------+

By default, NumPy's ``np.loadtxt`` routine returns this organization for columnar files. In
the example code below, we load the example data file `random_walk_sample_0.txt.gz
<https://github.com/pdebuyl-lab/tidynamics/raw/master/examples/random_walk_sample_0.txt.gz>`_
in the variable ``pos`` and compute the corresponding mean-square displacement with
tidynamics.

.. code:: python

   import numpy as np
   import tidynamics
   pos = np.loadtxt('random_walk_sample_0.txt.gz')
   msd = tidynamics.msd(pos)
