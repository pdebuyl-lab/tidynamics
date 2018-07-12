---
title: 'tidynamics: A tiny package to compute the dynamics of stochastic and molecular simulations'
tags:
- physics
- time series
- stochastic processes
authors:
- name: Pierre de Buyl
  orcid: 0000-0002-6640-6463
  affiliation: 1
affiliations:
- name: Instituut voor Theoretische Fysica, KU Leuven, B-3001 Leuven, Belgium 
  index: 1
date: 20 June 2018
bibliography: paper.bib
---

# Summary

tidynamics provides an efficient implementation of the Fast Correlation Algorithm to compute
correlation functions of interest in molecular [@allen_tildesley_1987;@nmoldyn_1995] and
stochastic [@gardiner_2004] dynamics.
The autocorrelation, the correlation between two time-series, the mean-square displacement,
and the cross-displacement (for off-diagonal realisations of Brownian motion), allow the
quantitative measure of relaxation and transport coefficients from numerical trajectories.

tidynamics is designed as a library in which every routine operates directly on NumPy arrays
and returns NumPy arrays. The interface is simple and enables convenient use in interactive
sessions or in teaching material. We test the library against Python 2.7, 3.5 and 3.6 and
several versions of NumPy to guard against a possible sensitivity to the API.

The Fast Correlation Algorithm relies on the Fourier transform to compute correlations. For
this purpose, we use NumPy's [@travis_numpy_2006] FFT module `np.fft`.
The advantage of using Fourier transforms is a reduced computational cost in comparison to a
direct loop over the data. We expect a scaling of the CPU time $t_\mathrm{CPU}$ of
$t_\mathrm{CPU} \propto N \log N$ where $N$ is the length of the time series. We show the
actual CPU time and compare it favourably to the expected scaling in the example *Scaling
behaviour*.

NumPy [@travis_numpy_2006] and SciPy [@scipy-web] implement correlation routines as well. In
the case of NumPy, the computation is based on a direct loop with a quadratic scaling of the
CPU time $O(N^2)$. In SciPy, both the direct and a Fourier transform version are
implemented.

The definition of `np.correlate` and `scipy.signal.correlate` differs from the definition
traditionally used in dynamical systems in two ways. These routines do not correct for
aperiodic signals, an issue that is addressed in the Fast Correlation Algorithm by
zero-padding the signal, and they do not normalise the result by the actual number of
samples. In addition to these differences, the relative complexity of building SciPy and its
larger size motivated us to rely on NumPy only.  NumPy and SciPy do not provide functions to
compute the mean-square displacement of trajectories. The Fast Correlation Algorithm as
applied to mean-square displacements was proposed in [@nmoldyn_1995] and is less known than
the plain correlation algorithm.

The benefits of using tidynamics originate in the implementation of the suitable definitions
for the study of dynamical systems, in a good performance, and in its ease of installation.


# Acknowledgements

Pierre de Buyl is a postdoctoral fellow of the Research Foundation Flanders - FWO.

# References
