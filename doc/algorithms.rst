Algorithms
==========

tidynamics relies on the Fast Correlation Algorithm (FCA) that was proposed in the context
of molecular simulations by Kneller et al :cite:`nmoldyn_1995` and that was included in the
software `nMOLDYN <http://dirac.cnrs-orleans.fr/nMOLDYN.html>`_. For the full explanation,
see the article or nMOLDYN's user manual. We provide here an overview of the algorithms.

The FCA results in the same numerical values for correlation functions as running explicitly
an average over all pairs of points at a computational cost of :math:`O(N \log N)` instead
of :math:`O(N^2)` where :math:`N` is the length of the time series. For a brief illustration
of correlation algorithms, see this blog post `<http://pdebuyl.be/blog/2016/correlators.html>`_

By using `NumPy <http://www.numpy.org/>`_ for all operations, the overhead of using an
interpreted language is reduced and the advantage of the FCA in terms of computational
complexity makes is feasible to analyze realistic datasets in memory, for instance in an
interactive `IPython <http://ipython.org/>`_ terminal or a `Jupyter <http://jupyter.org/>`_
notebook.

Correlations
------------

The correlation :math:`C_{AB}(\tau)` is

.. math::
   C_{AB}(\tau) = \langle A(0) B(\tau) \rangle

where the angle brackets denote an average over time.

For correlations, the FCA relies on a slight modification of the `Convolution theorem
<https://en.wikipedia.org/wiki/Convolution_theorem>`_ in which one convolves a time series
with its time-reversed counterpart.

One important point of attention in the algorithm consists in padding the data with zero
values, as else the result contains the correlation of the signal with its periodic
image.

Mean-Square Displacements
-------------------------

The mean-square displacement :math:`MSD(\tau)` is

.. math::
   MSD(\tau) = \langle (x(\tau) - x(0) )^2 \rangle

where the angle brackets denote an average over time.

The computation of the MSD relies on decomposing the average into an average term and an
explicit correlator:

.. math::
   \langle x(\tau)^2 + x(0)^2 \rangle - 2\langle x(\tau) x(0) \rangle

The correlator is computed with the convolution theorem and the other operations have linear
complexity. The finite length of the time series is also taken into account in the
algorithm.

Cross displacements
-------------------

The cross displacement :cite:`kraft_complex_shape_2013` :math:`C_{ij}(\tau)` is

.. math::
   C_{ij}(\tau) = \langle (x_i(\tau) - x_i(0)) (x_j(\tau) - x_j(0)) \rangle

As for the mean-square displacement, the interest of using tidynamics lies in the fast
computation of the correlation part.
