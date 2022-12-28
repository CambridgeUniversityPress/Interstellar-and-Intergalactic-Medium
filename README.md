# *Interstellar and Intergalactic Medium*

Jupyter notebooks, python code, and selected data files and sources for the figures from Ryden &amp; Pogge, 
[*Interstellar and Intergalactic Medium*](https://www.cambridge.org/highereducation/books/interstellar-and-intergalactic-medium/A647BECF975E19E86F7F88F7BB103AA7).

[!["ISM/IGM Cover"](Misc/ISMIGM_Cover_512.png?raw=true "Interstellar and Intergalactic Medium")](https://www.cambridge.org/highereducation/books/interstellar-and-intergalactic-medium/A647BECF975E19E86F7F88F7BB103AA7)

## Overview
*Interstellar and Intergalactic Medium* by Barbara S. Ryden and Richard W. Pogge is the first volume in *The Ohio State Astrophysics Series* of 
textbooks published by Cambridge University Press.  The audience for this series is graduate students and upper-level undergraduates studying astronomy and physics.

Most of the figures in this book were created by the authors, the majority of which are plots of data or calculations made using
Python programs implemented as Jupyter notebooks. We are making all of these notebooks available on GitHub as an ancillary 
to the book.

Instructors and students using *Interstellar and Intergalactic Medium* are welcome to use these notebooks to make high-resolution versions
of the book figures for presentations, adapt them for use in class, or to use as the basis for problem sets or projects in courses adopting this
book.  Over time we hope to collect and present other notebooks that will enable further explorations of topics in the book, become
part of computational problem sets or individual and group projects, etc. This way, the figures become a starting point for learning
and new explorations rather than being frozen into print.

## Software Requirements

All notebooks were developed in Python 3 using the [Anaconda Python distribution](https://www.anaconda.com). 

Required packages are numpy, scipy, pandas, matplotlib, and astropy, all available with Anaconda.

LaTeX is required for math symbols in the notebooks.

There are two packages used for a few of the figures that are not part of the Anaconda distribution:

 * HEALPix format FITS files require use of [healpy](https://github.com/healpy/healpy) (e.g., for all-sky map data in Chapters 1, 3, and 7).

 * Nebular emission-line calculations in Chapter 4 use [PyNeb](https://github.com/Morisset/PyNeb_devel).
 
If needed, these packages can be installed following the instructions on the project websites listed.

### Optional Packages

Collisional Ionization Equilibrium calculations were performed using [ChiantiPy](https://github.com/chianti-atomic/ChiantiPy/) and the 
[CHIANTI Atomic Database](https://www.chiantidatabase.org/).  Because CHIANTI calculations are time-consuming, we include pre-calculated data sets
with the corresponding Jupyter notebooks. Those wishing to explore CIE beyond the parameters we chose for the figures in the book will need to install the 
full CHIANTI database and the ChiantiPy package. **CHIANTI and ChiantiPy are not required to use these notebooks.**  We've included the code we used
to generate the pre-computed data files as worked examples of using CHIANTI and ChiantiPy.

## Downloads

### Download and Install

To download a copy of this repository onto your local computer, go to the folder on your computer where you want to install it and type

> `git clone https://github.com/CambridgeUniversityPress/Interstellar-and-Intergalactic-Medium`

This will create the `Interstellar-and-Intergalactic-Medium` folder containing the entire repository.  You may rename this repository after
installation to shorten the name if you wish (e.g., `/path/to/wherever/ISM_IGM`).

### Update the notebooks and data

To update your copy, go into the top-level folder you created above (e.g., `/path/to/wherever/ISM_IGM`) and type

> `git pull`

If there are no updates, your local copy will be unaffected.

## Use and Attribution

The notebooks and their contents are original works of the authors and often include data obtained from public archives or from 
professional colleagues (always from published sources).  We ask that users preserve all literature citations to the original work
from which such data were derived, and give proper credit when using them. If you use these notebooks, please make
reference to the *Interstellar and Intergalactic Medium* book and this repository.

### License Notice

All files in this repository are licensed under a [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/), to 
foster broader use of the notebooks and their data by teachers and students.
