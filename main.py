# Script to make a Taylor diagram from LEM inputs
# Geo.X hackathon 13/03/18

import gdalio as gdal_io
import numpy as np
import matplotlib.pyplot as plt
from differences import *

# read in the raster
DataDirectory = '../CAESAR_data/'
InitialFileName = 'D4elev.dat76212001.txt'
Filename_TS1 = 'D4elev.dat73584003.txt'
Filename_TS2 = 'D4elev.dat110376000.txt'

print ("Reading in the raster data...")

# these are np.arrays with the raster data
InitialTopoArray = gdal_io.ReadRasterArrayBlocks(DataDirectory+InitialFileName,raster_band=1)
TimeStep1Array = gdal_io.ReadRasterArrayBlocks(DataDirectory+Filename_TS1,raster_band=1)
TimeStep2Array = gdal_io.ReadRasterArrayBlocks(DataDirectory+Filename_TS2,raster_band=1)

# strip the nans
InitialTopoArray = InitialTopoArray[np.logical_not(np.isnan(InitialTopoArray))]
TimeStep1Array = TimeStep1Array[np.logical_not(np.isnan(TimeStep1Array))]
TimeStep2Array = TimeStep2Array[np.logical_not(np.isnan(TimeStep2Array))]

print np.shape(InitialTopoArray)
print len(TimeStep1Array)
print len(TimeStep2Array)

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

plt.subplot(3,1,3)
plt.plot(refdata)
plt.show()

