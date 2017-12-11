tidynamics
==========

A tiny package to compute the dynamics of stochastic and molecular simulations.

:License: BSD 3-clause
:Author: Pierre de Buyl
:Website: http://lab.pdebuyl.be/tidynamics/

tidynamics

- performs the computation of mean-square displacements and correlation functions.
- accepts as input NumPy arrays storing the positions and velocities of particles.
- implements the so-called Fast Correlation Algorithm proposed by Kneller and others for the
  `nMOLDYN <http://dirac.cnrs-orleans.fr/plone/software/nmoldyn/>`_ analysis program.
- depends only `Python <https://www.python.org/>`_ and `NumPy <http://www.numpy.org/>`_.

For a quick jump into tidynamics, have a look at the examples.

The development of tidynamics is in early stages but it features several tests.

Goals:

- Minimal dependencies.
- Serve as a reference implementation for common algorithms that are useful for molecular
  and stochastic simulations.

