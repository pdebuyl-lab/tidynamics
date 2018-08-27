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

tidynamics provides an efficient implementation of the Fast Correlation Algorithm (FCA) to
compute correlation functions of interest in molecular [@allen_tildesley_1987;@nmoldyn_1995]
and stochastic [@gardiner_2004] dynamics.
Building on the FCA, tidynamics computes the autocorrelation (the correlation of a time
series with itself), the correlation between two time-series, the mean-square displacement
of a trajectory, and the cross-displacement (for off-diagonal realisations of Brownian
motion).
These correlation functions serve for the quantitative measure of relaxation and transport
coefficients from numerical trajectories.

There is a lack of a self-contained implementation of the algorithm. The software nMoldyn
[@hinsen_nmoldyn3_2012] implements it within a larger library but it has a more complex
interface and more dependencies. The goal of tidynamics is to serve as a reference
implementation with a lighter interface.

tidynamics is designed as a library in which every routine operates directly on NumPy arrays
and returns NumPy arrays. The interface is simple and enables convenient use in interactive
sessions or in teaching material. We test the library against Python 2.7, 3.5, and 3.6 and
several versions of NumPy to guard against a possible sensitivity to the API.

The Fast Correlation Algorithm relies on the Fourier transform to compute correlations. For
this purpose, we use NumPy's [@oliphant_cise_2007] FFT module `np.fft`.
The advantage of using Fourier transforms is a reduced computational cost in comparison to a
direct loop over the data. We expect a scaling of the CPU time $t_\mathrm{CPU}$ of
$t_\mathrm{CPU} \propto N \log N$ where $N$ is the length of the time series. We show in
Figure 3 the actual CPU time and compare it favourably to the expected scaling in the
example *Scaling behaviour*.

NumPy [@oliphant_cise_2007] and SciPy [@scipy-web] implement correlation routines as well. In
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
applied to mean-square displacements was proposed by @nmoldyn_1995 and is less known than
the plain correlation algorithm.

The benefits of using tidynamics originate in the implementation of the suitable definitions
for the study of dynamical systems, good performance, and its ease of installation.

# Examples

We show in Figures 1, 2, and 3 the examples provided with tidynamics. The examples in the
repository include short codes for a random walk, for the Ornstein-Uhlenbeck process, and
for the scaling performance analysis of the autocorrelation routine.

![Mean-square displacement for a random walk and for a trajectory at constant velocity.](msd_example.pdf)

![Velocity autocorrelation function for a Ornstein-Uhlenbeck process [@gardiner_2004].](vacf_example.pdf)

![Scaling of the CPU time with respect to the length of the data.](scaling.pdf)

# Acknowledgements

PdB is a postdoctoral fellow of the Research Foundation Flanders - FWO.
PdB would like to acknowledge useful discussions with Konrad Hinsen and feedback about the
library from Max Linke.

# References
