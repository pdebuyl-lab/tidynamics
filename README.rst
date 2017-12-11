tidynamics
==========

A tiny package to compute the dynamics of stochastic and molecular simulations.

tidynamics depends only on `Python <https://www.python.org/>`_ and `NumPy
<http://www.numpy.org/>`_ and performs the computation of

- Mean-square displacements
- Correlation functions

tidynamics accepts as input NumPy arrays storing the positions and velocities of particles.

tidynamics relies on the so-called Fast Correlation Algorithm proposed by Kneller and others
for the `nMOLDYN <http://dirac.cnrs-orleans.fr/plone/software/nmoldyn/>`_ analysis program.

The development of tidynamics is in early stages but it features several tests.

:License: BSD 3-clause
:Author: Pierre de Buyl
:Website: http://lab.pdebuyl.be/tidynamics/

