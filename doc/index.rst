.. tidynamics documentation master file, created by
   sphinx-quickstart on Sat Dec  9 22:10:27 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

tidynamics
==========

.. only:: html

   .. image:: http://joss.theoj.org/papers/c4784e48e7514c207d95f440c2a07874/status.svg
      :target: http://joss.theoj.org/papers/c4784e48e7514c207d95f440c2a07874
      :alt: JOSS review page

   .. image:: https://travis-ci.org/pdebuyl-lab/tidynamics.svg?branch=master
      :target: https://travis-ci.org/pdebuyl-lab/tidynamics
      :alt: Test status

   .. image:: https://anaconda.org/conda-forge/tidynamics/badges/version.svg
      :target: https://anaconda.org/conda-forge/tidynamics
      :alt: Link to conda-forge page

   .. image:: https://mybinder.org/badge.svg
      :target: https://mybinder.org/v2/gh/pdebuyl-lab/tidynamics/master?filepath=doc%2Findex.ipynb
      :alt: Link to binder example notebook


.. only:: latex

    Introduction
    ------------


A tiny package to compute the dynamics of stochastic and molecular simulations.

:License: BSD 3-clause
:Author: Pierre de Buyl
:Website: http://lab.pdebuyl.be/tidynamics/
:Version: |release|

tidynamics

- performs the computation of mean-square displacements and correlation functions.
- accepts as input NumPy arrays storing the positions and velocities of particles.
- implements the so-called Fast Correlation Algorithm proposed by Kneller and others
  :cite:`nmoldyn_1995` for the `nMOLDYN
  <http://dirac.cnrs-orleans.fr/plone/software/nmoldyn/>`_ analysis program.
- depends only `Python <https://www.python.org/>`_ and `NumPy <http://www.numpy.org/>`_.

For a quick jump into tidynamics, have a look at the examples.

Goals and plans:

- Minimal dependencies.
- Serve as a reference implementation for common algorithms that are useful for molecular
  and stochastic simulations.
- Provide later a bit more flexibility to handle cross correlations and many-body systems.


Installation
------------

It is necessary to have Python and NumPy to install and use tidynamics.

tidynamics can be installed with pip::

    pip install --user tidynamics

or with conda (via conda-forge)::

    conda install -c conda-forge tidynamics

It is also possible to download the source code and execute the setup.py file.

I ran the tests with Python 2.7, 3.5 and 3.6 and NumPy 1.11 and 1.13. If you encounter any
issue, let me know (see :ref:`Contact` below).

Testing
-------

We use `pytest <https://pypi.python.org/pypi/pytest/>`_ for testing::

    python -m pytest

Installing tidynamics does not install the tests. It is necessary to download tidynamics'
source and to install pytest to run the tests.

.. _contact:

Contact, support, and contribution information
----------------------------------------------

To contact the author about tidynamics, you can either write an email to `Pierre de Buyl
<https://www.kuleuven.be/wieiswie/nl/person/00092351>`_ or use the `issue tracker
<https://github.com/pdebuyl-lab/tidynamics/issues>`_ of the GitHub project.

Bug reports are welcome. If you consider proposing a feature, please keep in mind the goals
and plans exposed above.

Contributors are listed in :ref:`contributors`.
