# Molecular Hydrogen Electronic State Data

Copies of the moleular hydrogen (H<sub>2</sub>) potential curves and vibrational energy levels tabulated by
[Sharp, 1971, Atomic Data, 2, 119](https://ui.adsabs.harvard.edu/abs/1971AD......2..119S), used by figures
for chapter 7 of Ryden and Pogge *Interstellar and Intergalactic Medium*.

This folder should reside in the same folder as the Jupyter notebooks for Chapter 7 figures.

## Contents:

We provide copies of the data for the ground state and first two excited electronic states
of H<sub>2</sub>:
<dl>
 <dd>H2_1Sigma_g+_potl.dat and H2_1Sigma_g+_v.dat: electronics ground state
 <dd>H2_1Sigma_u+_potl.dat and H2_1Sigma_u+_v.dat: first electronic state (Lyman bands)
 <dd>H2_1Pi_u_potl.dat and H2_1Pi_u_v.dat: second electronic state (Werner bands)
 
For each state, there are two multi-column ASCII text files, as follows::

Potential curve: potl.dat:
 * interproton distance, r, in Angstroms
 * potential energy, V(r), in eV
 
Vibrational levels: v.dat:
 * v = vibrational quantum number
 * eV = energy in eV
 * Rmin = minimum interproton distance in Angstroms
 * Rmax = maximum interproton distance in Angstroms
 
## Revision History

* v1.0 - 2021 Jan 8, first version in advance of publication [rwp/osu]


