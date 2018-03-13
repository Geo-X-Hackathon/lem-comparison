# Script to make a Taylor diagram from LEM inputs
# Geo.X hackathon 13/03/18

import gdalio as gdal_io
import numpy as np
import matplotlib.pyplot as plt
from differences import *
from input_dem import *
from correlation import *
from taylorDiagram import *


# define the filenames
DataDirectory = '../Caesar-Ddata/'
InitialFileName = 'DEM_init.txt'
RefFileName = 'A1-210.txt'
Filename_TS1 = 'D1-210.txt'
Filename_TS2 = 'D2-210.txt'
Filename_TS3 = 'D3-210.txt'
Filename_TS4 = 'D4-210.txt'

# get the initial DEM
InitialDEM = ReadInitialDEM(DataDirectory+InitialFileName)

# get the reference DoD and std
RefDod, RefStd = ReadReference(InitialDEM,DataDirectory+RefFileName)
print(RefDod)
print(RefStd)

# now for each other DEM, calculate the pearson correlation and standard deviation

#create figure
fig = plt.figure(figsize=(10, 4))
dia = TaylorDiagram(RefStd, fig=fig, rect=122, label="Reference")

# Add grid
dia.add_grid()

# Add RMS contours, and label them
contours = dia.add_contours(colors='0.5')
PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')

pointcp, pointsd = CalculateTaylorPoint(DataDirectory+Filename_TS1,InitialDEM,RefDod)
dia.add_sample(pointsd, pointcp, marker='o', ms=6, ls='', mfc='r', mec='k')

pointcp, pointsd = CalculateTaylorPoint(DataDirectory+Filename_TS2,InitialDEM,RefDod)
dia.add_sample(pointsd, pointcp, marker='o', ms=6, ls='', mfc='g', mec='k')

pointcp, pointsd = CalculateTaylorPoint(DataDirectory+Filename_TS3,InitialDEM,RefDod)
dia.add_sample(pointsd, pointcp, marker='o', ms=6, ls='', mfc='b', mec='k')

pointcp, pointsd = CalculateTaylorPoint(DataDirectory+Filename_TS4,InitialDEM,RefDod)
dia.add_sample(pointsd, pointcp, marker='o', ms=6, ls='', mfc='k', mec='r')