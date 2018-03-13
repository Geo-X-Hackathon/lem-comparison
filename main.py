# Script to make a Taylor diagram from LEM inputs
# Geo.X hackathon 13/03/18

import gdalio as gdal_io
import numpy as np
import matplotlib.pyplot as plt
from differences import *
from input_dem import *
from correlation import *
from taylorDiagram import *
from glob import glob

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
fig = plt.figure(figsize=(10, 5))
dia = TaylorDiagram(RefStd, fig=fig, rect=121, label="Reference")

dia2 = TaylorDiagram(RefStd, fig=fig, rect=122, label="Reference")

# Add grid
dia.add_grid()
dia2.add_grid()

# Add RMS contours, and label them
contours = dia.add_contours(colors='0.5')
PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')
contours = dia2.add_contours(colors='0.5')
PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')

# for each model run, get all the files and plot them onto the diagram

# D1
files = sorted(glob(DataDirectory+'D1*.txt'))
n_files = len(files)
colors = plt.matplotlib.cm.Reds(np.linspace(0.1, 0.9, n_files))
for i, DEMFileName in enumerate(files):
    print DEMFileName
    pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
    dia.add_sample(pointsd, pointcp, marker='o', ms=10, ls='', mfc=colors[i], mec='k')

# D3
files = sorted(glob(DataDirectory+'D3*.txt'))
colors = plt.matplotlib.cm.Blues(np.linspace(0.1, 0.9, n_files))
for i, DEMFileName in enumerate(files):
    pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
    dia.add_sample(pointsd, pointcp, marker='o', ms=10, ls='', mfc=colors[i], mec='k')

# D2
files = sorted(glob(DataDirectory+'D2*.txt'))
colors = plt.matplotlib.cm.Greens(np.linspace(0.3, 0.7, n_files))

for i, DEMFileName in enumerate(files):
    pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
    dia2.add_sample(pointsd, pointcp, marker='o', ms=10, ls='', mfc=colors[i], mec='k')

# D4
files = sorted(glob(DataDirectory+'D4*.txt'))
colors = plt.matplotlib.cm.Wistia(np.linspace(0.3, 0.7, n_files))

for i, DEMFileName in enumerate(files):
    pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
    dia2.add_sample(pointsd, pointcp, marker='o', ms=10, ls='', mfc=colors[i], mec='k')

plt.show()
