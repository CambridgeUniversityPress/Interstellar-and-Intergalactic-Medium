# Chapter 9: Diffuse Intergalactic Medium

Figures from Chapter 9 of Ryden & Pogge, *Interstellar and Intergalactic Medium*.

## Jupyter Notebooks:
<dl>
<dd>Figure 9.1 - Spectra of the quasars 3C 273 and Q1422+2309
<dd>Figure 9.2 - Spectra of two quasars at z=5.774 and z=6.016
<dd>Figure 9.4 - Effective optical depth for Lyman-alpha as a function of redshift
<dd>Figure 9.5 - Effect of reionization on the CMB power spectrum
<dd>Figure 9.6 - Cosmic star formation rate as a function of redshift
<dd>Figure 9.7 - Strongly damped Lyman-alpha line in quasar QSO J021741.8-370100
</dl>

## Data Files:

Some of the Jupyter notebooks for this chapter have external data files that should be stored in the same
folder as the notebooks.  In all cases the individual notebooks describe the contents of the data files, 
and all data files have explanatory comment headers.

### Figure 9.1
Data provided by William Keel, the University of Alabama, Department of Astronomy
* **3C273_STIS.txt** - HST STIS UV spectrum of quasar 3C273: 2-column ASCII text
* **Q1422B10.txt** - Optical spectrum of quasars Q1422+2307 (z=3.62): 2-column ASCII text

### Figure 9.2
Data provided by Xiaohui Fan and Feige Wang, University of Arizona, Department of Astronomy. 
Originally published as [Fan et al. 2001, AJ, 122, 2833](https://ui.adsabs.harvard.edu/abs/2001AJ....122.2833F)
* **J0836+0054_ESI.txt** - Keck ESI spectrum of J0836+0054: 3-column ASCII text
* **J1306+0356_ESI.txt** - Keck ESI spectrum of J1306+0356: 3-column ASCII text

### Figure 9.4
Optical depths derived from data in [Bosman et al. 2018, MNRAS, 479, 1055](https://ui.adsabs.harvard.edu/abs/2018MNRAS.479.1055B),
Table 5, using equations 3 and 4 of their paper to convert their measurements into mean effective optical depth.
* **Bosman_highz_tau.txt** - Derived optical depth as a function of redshift: 3-column ASCII text

### Figure 9.5
The data are pre-computed by the authors using [CAMB](https://camb.info/) and the  
[CAMB Web Interface](https://lambda.gsfc.nasa.gov/toolbox/tb_camb_form.cfm) at NASA Goddard Space Flight Center's
Legacy Archive for Microwave Background Data Analysis ([LAMBDA](https://lambda.gsfc.nasa.gov/)). The output
files from CAMB were then merged into this single data file:
* **CAMB_tau_e.txt** - CMB Power Spectrum: 6-column ASCII text

### Figure 9.7
Data are from the ESO UVES spectrograph obtained from the [ESO Science Archive Facility](http://archive.eso.org), 
Table spectrum_qso_34.424-37.017.tbl, along with a model of the damped Lyman-alpha absorption
calculated by Stephan Frank, Ohio State University, Department of Astronomy.
* **J021741.8-370100_norm.txt** - ESO UVES observed Lyman-alpha spectrum and model: 3-column ASCII text

## Revision History

* 2021 Jan 18, first version in advance of publication [rwp/osu]


