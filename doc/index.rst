.. tidynamics documentation master file, created by
   sphinx-quickstart on Sat Dec  9 22:10:27 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

tidynamics
==========

.. only:: html

   .. image:: http://joss.theoj.org/papers/10.21105/joss.00877/status.svg
      :target: https://doi.org/10.21105/joss.00877
      :alt: DOI link to JOSS article

   .. image:: https://github.com/pdebuyl-lab/tidynamics/actions/workflows/test.yml/badge.svg
      :target: https://github.com/pdebuyl-lab/tidynamics/actions/workflows/test.yml
      :alt: Test status

   .. image:: https://anaconda.org/conda-forge/tidynamics/badges/version.svg
      :target: https://anaconda.org/conda-forge/tidynamics
      :alt: Link to conda-forge page

   .. image:: https://mybinder.org/badge.svg
      :target: https://mybinder.org/v2/gh/pdebuyl-lab/tidynamics/master?filepath=doc%2Findex.ipynb
      :alt: Link to binder example notebook

   .. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1401184.svg
      :target: https://doi.org/10.5281/zenodo.1401184
      :alt: Link Zenodo archive


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
  <http://dirac.cnrs-orleans.fr/nMOLDYN.html>`_ analysis program.
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

It is also possible to download the source code and execute pip locally.

Tests are run with Python 3.7 to 3.11. Python 2 is not supported anymore.  If
you encounter any issue, let me know (see :ref:`Contact` below).


Citation
--------

When using tidynamics in a publication, please cite the following paper:

Pierre de Buyl (2018), *tidynamics: A tiny package to compute the dynamics of
stochastic and molecular simulations*, The Journal of Open Source
Software https://doi.org/10.21105/joss.00877

The BibTeX entry can be found in :download:`CITATION <../CITATION>`.

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
