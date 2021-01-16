# Chapter 5: Hot Ionized Medium

Figures from Chapter 5 of Ryden & Pogge, *Interstellar and Intergalactic Medium*.

## Contents:

### Jupyter Notebooks:
<dl>
<dd>Figure 5.4 - Sedov–Taylor solution for a spherical blastwave with gamma = 5/3.
<dd>Figure 5.6 - Ion fractions for carbon and oxygen in collisional ionization equilibrium (CIE).
<dd>Figure 5.7 - Total cooling function (line+continuum) for gas in CIE.
<dd>Figure 5.8 - Simulated spectrum of solar-metallicity, low-density gas in CIE.
<dd>Figure 5.9 - Location in galactic coordinates of nearby hot DA white dwarfs.
</dl>

## Data Files:

Figures 5.6 through 5.9 and have accompanying data files that should be stored 
in the same folder as the corresponding Jupyter notebooks.

### Figure 5.6
* ionFrac_C.txt: Ion fractions of carbon vs. Temperature in CIE, 8-column ASCII text
* ionFrac_O.txt: Ion fractions of oxygen vs. Temperature in CIE, 10-column ASCII text

### Figure 5.7
* solarCooling.txt: CIE cooling function for solar-metallicity gas, 16-column ASCII text.

### Figure 5.8
* cieSpectrum.txt: X-ray spectrum of low-density solar-metallicity gas in CIE, 9-column ASCII text.

### Figure 5.9
* sl2006_wd.txt: Locations of hot DA white dwarfs with OVI absorption-line detections or upper limits from [Savage & Lehner 2006, ApJS, 162, 134](https://ui.adsabs.harvard.edu/abs/2006ApJS..162..134S), Tables 1 and 3.  6-column ASCII text.

## CHIANTI Atomic Database CIE calculations

Collisional ionization equilibrium (CIE) calculations for this book were performed using 
[ChiantiPy](https://github.com/chianti-atomic/ChiantiPy/) and the [CHIANTI atomic database](https://www.chiantidatabase.org/). If you want to reproduce these
calculations or go beyond the pre-calculated data sets for the notebooks above, we provide notebooks and standalone python scripts that show how we did this.
Note that to use these you must have updated versions of both ChiantiPy and the CHIANTI database installed before using them, and that some of the calculations
can be very time-consuming as noted below.

### Figure 5.6:
 * ionFrac_Calc.ipynb: Jupyter notebook to use ChiantiPy and CHIANTI to compute and plot the ion fractions of carbon and oxygen in-situ rather than reading pre-calculated 
 data from external files.  This calculation is relatively fast.
 * ionFrac_Table.ipynb: uses ChiantiPy and CHIANTI to compute the ion fraction of a given species then export the data as an ASCII multi-column table. A version of this notebook was used to create the pre-computed data files for the Figure 5.6 notebook above.

### Figure 5.7:
* cieCooling.py: standalone python program to compute a cooling curve with ChiantiPy and CHIANTI for gas in CIE at a given density and metallicity.  Creates an ASCII multi-column
table with the total cooling function and all of its components. The computation that created the solarCooling.txt file included above took about 2 hours on an 3.2GHz Core i5
iMac.

### Figure 5.8:
* cieSpec_Calc.ipynb: Jupyter notebook to use ChiantiPy and CHIANTI to compute the X-ray spectrum of gas in CIE and 
create an output ASCII text file with the spectrum and its components. The calculation time can be many minutes.


## Revision History

* v1.0 - 2021 Jan 16, first version in advance of publication [rwp/osu]


