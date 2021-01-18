# Chapter 6: Interstellar Dust

Figures from Chapter 6 of Ryden & Pogge, *Interstellar and Intergalactic Medium*.

## Contents:

### Jupyter Notebooks:
<dl>
<dd>Figure 6.2 - Replotting of Trumpler's 1930 Angular-diameter distance versus luminosity distance for 100 open clusters.
<dd>Figure 6.3 - Clayton, Cardelli, and Mathis (1989) interstellar extinction curve
<dd>Figure 6.4 - Real and imaginary indices of refraction of silicon at T=300K
<dd>Figure 6.5 - Efficiency factor Q_ext for two values of the real index of refraction
<dd>Figure 6.6 - Reflectance spectra of olivine, pyroxene, and carbon
<dd>Figure 6.7 - Infrared spectrum of embedded young stellar object RAFGL7009S (IRAS 18316-0602)
<dd>Figure 6.8 - 
<dd>Figure 6.10 - 
</dl>

### Images
The grayscale image in Figure 6.1 was scanned by the authors from the plate in an original bound
edition of the 1899 *Astrophysical Journal*, Volume 9. 
[Barnard, E.E., 1899, ApJ, 9, 157, Plate II](https://ui.adsabs.harvard.edu/abs/1899ApJ.....9..157B)
<dl>
  <dd>Figure 6.1: <b>Fig6_1_Barnard1899_PlateII.jpg</b> - Barnard's 1899 photograph of the Milky way near the star Theta Ophiuchi.  Rotated 90-degrees
  relative to the original for the book.
</dl>

## Data Files:

The Jupyter notebooks above have accompanying data files that should be stored 
in the same folder as the corresponding Jupyter notebooks.

### Figure 6.2
Data for luminosity and angular-diameter distances for 100 open star clusters from 
[Trumpler, R. 1930, Lick Observatory Bulletin #420, 14, 154](https://ui.adsabs.harvard.edu/abs/1930LicOB..14..154T), Table 3.  See the 
Jupyter notebook for what data were used. 
 * **Trumpler_GoodData.txt** - good open cluster distances, 2-column ASCII text
 * **Trumpler_BadData.text** - less-certain open cluster distances, 2-column ASCII text

### Figure 6.4
Data from [Green 2008, Solar Energy Materials and Solar Cells, 92, 1305](https://www.sciencedirect.com/science/article/pii/S0927024808002158), Table 1, intrinsic silicon at 300K.
 * **Green2008_Si300K.txt** - wavelength-dependent real and imaginary index of refraction, 4-column ASCII text.
 
### Figure 6.6
Reflectance spectra of olivine, pyroxene, and carbon at visible and near-infrared wavelengths from
the [USGS Spectral Library (splib07a)](https://crustal.usgs.gov/speclab/QueryAll07a.php), 
[Kokaly, R.F., et al. 2017, U.S. Geological Survey Data Series 1035, 61 p., https://doi.org/10.3133/ds1035](https://pubs.er.usgs.gov/publication/ds1035).
We've consolidated the data for these materials into single ASCII text files for convenience:
 * **Olivine_GDS80a.txt** - olivine optical/near-IR reflectance spectrum, 3-column ASCII text
 * **Bronzite_HS9.3b.txt** - pyroxene (bronzite) optical/near-IR reflectance spectrum, 3-column ASCII text
 * **Carbon_Black_GDS68.txt** - carbon optical/near-IR reflectance spectrum, 3-column ASCII text

See the Jupyter notebook and the individual file headers for detailed provenance information for each data set.

### Figure 6.7
Infrared spectrum of RAFGL7009S (IRAS 18316-0602), a young stellar object embedded behind ~40 magnitudes of dust extinction at optical wavelengths from 
[Dartois et al. 1998, A&A, 338, 21](https://ui.adsabs.harvard.edu/abs/1998A%26A...338L..21D).  Data are ISO archival SWS/LWS spectral data provided by 
Adwin Boogert (U. Hawaii).
 * **GL7009S_ISO.txt** - ISO SWS/LWS infrared flux spectrum of RAFGL7009S, 2-column ASCII text

### Figure 6.x
data for somehting
 * **filename** - description 


## Revision History

* v1.0 - 2021 Jan 17, first version in advance of publication [rwp/osu]
