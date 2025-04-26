# Chapter 10: Warm-Hot Intergalactic Medium

Figures from Chapter 10 of Ryden & Pogge, *Interstellar and Intergalactic Medium*.

## Jupyter Notebooks
<dl>
 <dd>Figure 10.2 - Redshift evolution of the baryonic mass fraction
 <dd>Figure 10.3 - Phase diagram of gas in the universe at redshift z=0
 <dd>Figure 10.4 - Redshift evolution of the mean metallicity of baryonic matter
 <dd>Figure 10.5 - Cooling function for atomic gas in CIE at a range of metallicities
 <dd>Figure 10.6 - <i>XMM-Newton X-ray Telescope</i> spectrum of the quasar 1ES 1553+113
</dl>

## Data Files

Some of the Jupyter notebooks for this chapter have external data files that should be stored in the same
folder as the notebooks.  In all cases the individual notebooks describe the contents of the data files, 
and all data files have explanatory comment headers.

### Figure 10.2
* **Martizzi_BaryonicMass.txt** - Baryonic mass fraction evolution data from [Martizzi et al. 2019, MNRAS, 486, 3766](https://ui.adsabs.harvard.edu/abs/2019MNRAS.486.3766M) Table 1: 5-column ASCII text. 

### Figure 10.3
* **Fig10_3_Martizzi_core.png** - Grayscale version of the TNG100 phase diagram from the right panel of
[Martizzi et al. 2019, MNRAS, 486, 3766](https://ui.adsabs.harvard.edu/abs/2019MNRAS.486.3766M) Figure 10.

### Figure 10.4
* **Martizzi_Metallicity.txt** - Metallicity of baryonic gas phases from [Martizzi et al. 2019, MNRAS, 486, 3766](https://ui.adsabs.harvard.edu/abs/2019MNRAS.486.3766M): 4-column ASCII text. 

### Figure 10.5 Cooling Functions
The cooling functions for a range of metallicities were computed using [ChiantiPy](https://github.com/chianti-atomic/ChiantiPy/) v0.9.5 and the
[CHIANTI atomic database](https://www.chiantidatabase.org/). This computation is very time-consuming (about 24 hours) so a separate program was used to 
perform the calcuations and we provide the computation results as a set of ASCII text files in the **Cooling/** folder that accompanies this notebook.
See the `README.md` file in the `Cooling/` folder for information.

### Figure 10.6
*XMM-Newton X-ray Telescope* Reflection Grating Spectrometer (RGS) spectra of quasar 1ES1553+113 from 
[Nicastro et al. 2018, Nature, 558, 406](https://ui.adsabs.harvard.edu/abs/2018Natur.558..406N), data provided by Sanskriti Das, The Ohio State University.

* **Nicastro2018_RGS1.txt** - XMM-Newton RGS1 spectrum of 1ES1553+113: 6-column ASCII text
* **Nicastro2018_RGS2.txt** - XMM-Newton RGS2 spectrum of 1ES1553+113: 6-column ASCII text

## Images

### Figure 10.1
Distributions of diffuse and warm-hot intergalactic gas from [Martizzi et al. 2019, MNRAS, 486, 3766](https://ui.adsabs.harvard.edu/abs/2019MNRAS.486.3766M),
using a color full-resolution of the original Figure 8 from that paper provided by Davide Martizzi. For the book we selected two panels from the uppr right 
and converted them to grayscale.
 * **Fig10_1_Martizzi.jpg**

## Revision History

* 2021 Jan 18, first version in advance of publication [rwp/osu]
