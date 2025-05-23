# Chapter 7: Molecular Clouds

Figures from Chapter 7 of Ryden & Pogge, *Interstellar and Intergalactic Medium*.

## Jupyter Notebooks
<dl>
  <dd>Figure 7.1 - Molecular Hydrogen ground state energy level diagram
  <dd>Figure 7.3 - All-sky map of the integrated line intensity of the CO J=1-0 transition
  <dd>Figure 7.5 - Molecular Hydrogen H2 Ground State and Lyman/Werner Bands
</dl>

## Data Files

Figures 7.1 and 7.5 use external files with molecular hydrogen potential curves and vibrational
energy levels tabulated by [Sharp, 1971, Atomic Data, 2, 119](https://ui.adsabs.harvard.edu/abs/1971AD......2..119S)
for the ground and first two excited electronic states.  These files are in the **H2** subfolder that accompanies these
notebooks.

### Figures 7.1 and 7.5
<dl>
  <dd><b>H2_1Sigma_g+_potl.dat</b> - ground state potential energy
  <dd><b>H2_1Sigma_g+_v.dat</b> - ground state vibrational energy levels
  <dd><b>H2_1Sigma_u+_potl.dat</b> - first excited state potential energy
  <dd><b>H2_1Sigma_u+_v.dat</b> - first excited state vibrational energy levels
  <dd><b>H2_1PI_u_potl.dat</b> - second excited state potential energy
  <dd><b>H2_1PI_u_v.dat</b> - second excited state vibrational energy levels.
</dl>
All are ASCII multi-column files.  See the README.md file in the H2 folder for details.

The data set for Figures 7.3 is too large for GitHub, so we provide links to the online sources here.  The data file needs to be
stored in the same folder as the corresponding Jupyter notebook and uncompressed.

### Figure 7.3 - Planck 2015 All-Sky WCO Emission Map
* [ESA Planck 2015 COMMANDER version](https://wiki.cosmos.esa.int/planckpla2015/index.php/CMB_and_astrophysical_component_maps#CO_line_emission) 
in HEALPix format, plotting the CO(1-0) amplitude posterior maximum in units K/km/sec. Source: [ESA Planck Legacy Archive](https://wiki.cosmos.esa.int/planck-legacy-archive)

## Literature Figures

### Figure 7.2
<sup>13</sup>CO and <sup>12</sup>CO emission lines in the galaxy M82 from [Paglionie et al. 2001, ApJS, 135, 183](http://ui.adsabs.harvard.edu/abs/2001ApJS..135..183P), 
Figure 1 middle panel.

## Revision History

* 2021 Jan 17, first version in advance of publication [rwp/osu]
* 2025 Apr 25, updated Figs 7.1 and 7.3 to use `pathlib` for transparent OS-agnostic path handling [rwp/osu]
