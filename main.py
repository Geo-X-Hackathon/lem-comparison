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
InitialFileName = 'DEM_init.txt'
RefFileName = 'A1-210.txt'
Filename_TS1 = 'D4-210.txt'
Filename_TS2 = 'C4-210.txt'

# get the initial DEM
InitialDEM = ReadInitialDEM(DataDirectory+InitialFileName)

# get the reference DoD and std
RefDod, RefStd = ReadReference(InitialDEM,DataDirectory+RefFileName)
print(RefDod)
print(RefStd)

# now for each other DEM, calculate the pearson correlation and standard deviation
