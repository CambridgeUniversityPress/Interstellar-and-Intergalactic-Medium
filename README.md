# Interstellar and Intergalactic Medium

Jupyter notebooks and source files for the figures from Ryden &amp; Pogge, *Interstellar and Intergalactic Medium*.

[(https://github.com/CambridgeUniversityPress/Interstellar-and-Intergalactic-Medium/blob/master/Misc/ISMIGM_Cover_1280.png?raw=true)](https://github.com/CambridgeUniversityPress/Interstellar-and-Intergalactic-Medium "Interstellar and Intergalactic Medium")

This repository is under construction and will be fully populated around the time the book appears in print in Spring of 2021.

## Overview
[*Interstellar and Intergalactic Medium*](https://www.cambridge.org/highereducation/books/interstellar-and-intergalactic-medium/A647BECF975E19E86F7F88F7BB103AA7)
by Barbara S. Ryden and Richard W. Pogge is the first volume in the *Ohio State Astrophysics Series* of textbooks to be 
published by Cambridge University Press.  The audience for this series is graduate students and upper-level 
undergraduates studying astronomy and physics.

Most of the figures in this book were created by the authors, the majority of which are plots of data or calculations made using
Python programs implemented as Jupyter notebooks. We are making all of these notebooks available on GitHub as an ancillary 
to the book, and will do this for all books in the series. GitHub will allow us to quickly update the notebooks
and provides ways for teachers and students to easily keep their copies up to date.

Instructors and students using *Interstellar and Intergalactic Medium* are welcome to use these notebooks to make high-resolution versions
of the book figures for presentation, adapt them for class, or use as the basis for problem sets or projects in courses adopting this
book.  Over time we hope to collect and present other notebooks that will enable further explorations of topics in the book, become
part of computational problem sets or individual and group projects, etc. This way, the figures become a starting point for learning
and new explorations rather than being frozen into print.

## Software Requirements

All notebooks were developed in Python 3 using the [Anaconda Python distribution](www.anaconda.com).  
Primary packages used are numpy, scipy, pandas, matplotlib, and astropy.

Additional packages used are as follows:

HEALPix format FITS files require use of [healpy](https://github.com/healpy/healpy) (e.g., for all-sky map data).

Nebular emission-line calculations use [PyNeb](https://github.com/Morisset/PyNeb_devel).

Collisional Ionization Equilibrium calculations were performed using [ChiantiPy](https://github.com/chianti-atomic/ChiantiPy/) and the 
[CHIANTI Atomic Database](https://www.chiantidatabase.org/).  Because CHIANTI calculations are time-consuming, we include pre-calculated
data sets. To explore beyond the parameters we chose for the illustrations in the book you need to install the full CHIANTI database 
and the ChiantiPy package.

## Use and Attribution

The notebooks and their contents are original works of the authors and often include data obtained from public archives or from 
professional colleagues (always from published sources).  We ask that users preserve all literature citations to the original work
from which such data were derived, and give proper credit when using them. If you use these notebooks, please make
reference to the *Interstellar and Intergalactic Medium* and this repository.

The notebooks themselves are licensed under ...
