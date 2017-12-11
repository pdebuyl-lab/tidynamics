Data format
===========

tidynamics assumes that the data is provided as NumPy arrays where the first dimension is
the time and the second dimension, if it exists, consists in the spatial coordinates of a
the trajectory.

Data is assumed to be sampled at equal time intervals.

Position data
-------------

For a 2D position dataset ``pos``, :math:`x(t)` is stored in ``pos[:,0]`` and :math:`y(t)`
is stored in ``pos[:,1]``.
