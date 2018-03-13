# Script to make a Taylor diagram from LEM inputs
# Geo.X hackathon 13/03/18

import gdalio as gdal_io
import numpy as np
import matplotlib.pyplot as plt
from differences import *
from input_dem import *
from correlation import *


# read in the raster
DataDirectory = '../CAESAR_data/'
InitialFileName = 'D4elev.dat76212001.txt'
Filename_TS1 = 'D4elev.dat73584003.txt'
Filename_TS2 = 'D4elev.dat110376000.txt'

(InitialTopoArray, TimeStep1Array, TimeStep2Array) = input_caesar1(DataDirectory,InitialFileName,Filename_TS1,Filename_TS2)

# differences for the raster arrays (as vectors)
diff1 = dem_difference(InitialTopoArray,TimeStep1Array)
diff2 = dem_difference(InitialTopoArray,TimeStep2Array)

plt.figure
plt.subplot(3,1,1)
plt.plot(diff1)
plt.subplot(3,1,2)
plt.plot(diff2)

# mean of differences
refdata = np.mean([diff1, diff2],axis = 0)

# get the pearson correlation coefficient and standard deviation
r1, std1 = pearson_correlation_std(refdata, diff1)
print("pearon_r1: ", r1)
print("std1: ", std1)

plt.subplot(3,1,3)
plt.plot(refdata)
plt.show()
