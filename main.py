# Script to make a Taylor diagram from LEM inputs
# Geo.X hackathon 13/03/18

import gdalio as gdal_io
import numpy as np
import matplotlib.pyplot as plt
from differences import *
from input_dem import *
from correlation import *


# define the filenames
DataDirectory = '../Caesar-Ddata/'
InitialFileName = 'D4elev.dat76212001.txt'
Filename_TS1 = 'D4elev.dat73584003.txt'
Filename_TS2 = 'D4elev.dat110376000.txt'

# get the initial DEM
InitialDEM = ReadInitialDEM(DataDirectory+InitialFileName)

# get the reference DoD and std
RefDod, RefStd = ReadReference(InitialDEM, RefFileName)
print(RefDod)
print(RefStd)

# now for each other DEM, calculate the pearson correlation and standard deviation
