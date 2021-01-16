#!/usr/bin/env python

'''cieCooling.py

Uses ChiantiPy to calculate and plot the radiative loss (aka cooling)
function for a plasma in CIE with Ne=0.004 cm^-3 and logT=4..7

Usage: cieCooling.py [options] [outFile]

where:
   outFile - ASCII file to write [default: cooling.txt]

Options:
  -f - force overwrite of existing output files [default: noclobber]
  -v - verbose debugging output [default: quiet]
  -V - print version info and exit
 --tmin - set minimum temperature [default: 1.e4]
 --tmax - set minimum temperature [default: 1.e7]
 --dt   - set logT step [default: 0.01]
 --ne   - set the electron density in cm^-3 [default: 0.004]
 --help - print usage and exit

Sources:
   ChiantiPy code: github.com/chianti-atomic/ChiantiPy
   CHIANTI atomic database: www.chiantidatabase.org

CHIANTI Citation: 
   CHIANTI is a collaborative project involving George Mason
   University, the University of Michigan, and the University of
   Cambridge (UK).


Author:
   R. Pogge, OSU Astronomy Dept.
   pogge.1@osu.edu
   2021 January 16 (last update)

'''

import sys
import os
import math
import getopt
import numpy as np 

# Throttle nuisance warnings

import warnings
warnings.filterwarnings('ignore',category=UserWarning, append=True)

# ChiantiPy

import ChiantiPy.core as ch
import ChiantiPy.tools.util as cu
import ChiantiPy.tools.data as cd

# Version and Date

verName = 'cieCooling v1.0'
verDate = '2021-01-16'
verbose = False
clobber = False

# Usage message

def printUsage():
    print('\nUsage: cieCooling.py [options] [outFile]')
    print('\nwhere:')
    print('  outFile - ASCII file to write [default: cooling.txt]')
    print('\nOptions:')
    print('  -f - force overwrite of existing output files [default: noclobber]')
    print('  -v - verbose debugging output [default: quiet]')
    print('  -V - print version info and exit')
    print(' --tmin - set minimum temperature [default: 1.e4]')
    print(' --tmax - set minimum temperature [default: 1.e7]')
    print(' --dt   - set logT step [default: 0.01]')
    print(' --ne   - set the electron density in cm^-3 [default: 0.004]')
    print(' --help - print usage and exit')

#----------------------------------------------------------------
#
# int2roman() - convert an integer to a roman number
#


def int2roman(arabic):
    '''
int2roman() - convert an integer to a roman number

Returns a string with the roman number equivalent of
an arabic integer.
    '''

    table = [['M',1000],['CM',900],['D',500],['CD',400],['C',100],
             ['XC',90],['L',50],['XL',40],['X',10],['IX',9],
             ['V',5],['IV',4],['I',1]]
    parts = []
    for letter, value in table:
        while value <= arabic:
            arabic -= value
            parts.append(letter)
    return ''.join(parts)
    
#----------------------------------------------------------------
#
# main program
#

minT = 1.e4  # minimum temperature in K, change with --tmin
maxT = 1.e8  # maximum temperature in K, change with --tmax
dlogT = 0.01 # log(T) step, change with --dt
ne = 0.004   # electron density in cm^-3.  Typical of local HIM bubble
minAbund = 2.e-5  # includes everything in spList

# Species we use and their Zs

spList = ['H','He','C','N','O','Ne','Mg','Si','S','Fe']
spZDict = {'h':1,'he':2,'c':6,'n':7,'o':8,'ne':10,'mg':12,
           'si':14,'s':16,'fe':26}


# Parse the command line

try:
    opts, files = getopt.gnu_getopt(sys.argv[1:],'vVfn:h',
                                    ['verbose','version','clobber',
                                     'tmin=','tmax=','dt=','help',
                                     'ne='])

except getopt.GetoptError as err:
    print(f'\n** ERROR: {err}')
    printUsage()
    sys.exit(1)

for opt, arg in opts:
    if opt in ('-V','--version'):
        print(f'{verName} ({verDate})')
        sys.exit(0)

    elif opt in ('-v','--verbose'):
        verbose = True

    elif opt in ('-f','--clobber'):
        clobber = True

    elif opt in ('--tmin'):
        minT = float(arg)

    elif opt in ('--tmax'):
        maxT = float(arg)
        
    elif opt in ('--dt'):
        dlogT = float(arg)

    elif opt in ('-n','--ne'):
        ne = float(arg)

    elif opt in ('-h','--help'):
        printUsage()
        sys.exit(0)

if len(files) > 0:
    outFile = files[0]
else:
    outFile = 'cooling.dat'

out = open(outFile,'w')

# Do the computation...

minLogT = math.log10(minT)
maxLogT = math.log10(maxT)
numT = 1+int((maxLogT-minLogT)/dlogT)
logT = np.linspace(minLogT,maxLogT,num=numT)
T = 10.0**logT # temperature (K)

# Do the calculation in CHIANTI

# Total Cooling curve, plus continuum contribuions

rl = ch.radLoss(T,ne,minAbund=minAbund)

# Total cooling in CIE, lines + continuum

totCool = rl.RadLoss['rate']
abundances=rl.RadLoss['abundance']

out.write(f'#\n')
out.write(f'# CIE cooling function for\n')
out.write(f'#   ne={ne:.3f} cm^-3\n')
out.write(f'#   logT = {logT[0]:.1f} to {logT[-1]:.1f}\n')
out.write(f'#   {abundances} abundances\n')
out.write(f'# Calculated using CHIANTI v9\n')
out.write(f'#\n')

header = '# T    Total    Cont   FFCont  FBCont  2PCont'

for species in spList:
    if len(species)==2:
        header += f'    {species}  '
    else:
        header += f'    {species}   '
header += '\n'
out.write(header)

# Continuum contribution: free-free, free-bound, and 2-photon

ffCool = rl.FreeFreeLoss
fbCool = rl.FreeBoundLoss
p2Cool = rl.TwoPhotonLoss

totCont = ffCool + fbCool + p2Cool

# Individual line contributions

spCool = {}
for species in spList:
    z=spZDict[species.lower()]
    ionList = []
    masterlist = cd.MasterList
    for ionstage in range(1,z+2):
        ionS = cu.zion2name(z,ionstage)
        ionSd = cu.zion2name(z,ionstage,dielectronic=1)
        if ionS in masterlist:
            ionList.append(ionS)
        if ionSd in masterlist:
            ionList.append(ionSd)
                
    rl = ch.radLoss(T,ne,ionList=ionList,doContinuum=0)
    spCool[species] = rl.RadLoss['rate']

# Now out to a big ASCII text file for later

for i in range(len(logT)):
    outStr = ''
    outStr += f'{logT[i]:.3f}'
    outStr += f' {math.log10(totCool[i]):.3f}' 
    outStr += f' {math.log10(totCont[i]):.3f}'
    outStr += f' {math.log10(ffCool[i]):.3f}' 
    outStr += f' {math.log10(fbCool[i]):.3f}' 
    outStr += f' {math.log10(p2Cool[i]):.3f}'
    for species in spList:
        outStr += f' {math.log10(spCool[species][i]):.3f}' 
    outStr += '\n'
    out.write(outStr)

out.close()
print(f'Done: output saved in {outFile}')

sys.exit(0)
