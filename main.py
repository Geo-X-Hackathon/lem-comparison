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



def test1():
    """
    Test 1: Taylor diagram for a single initial condition compared to a single reference case.
    """
    
    # define the FileNames
    DataDirectory = '../Caesar-Ddata/'
    InitialFileName = 'DEM_init.txt'
    RefFileName = 'A1-210.txt'
    
    # parameters
    Normalize = 0
    
    # get the initial DEM
    InitialDEM = ReadInitialDEM(DataDirectory+InitialFileName)
    
    # get the reference DoD and std
    RefDod, RefStd = ReadReference(InitialDEM,DataDirectory+RefFileName)
    #print(RefDod)
    #print(RefStd)
    
    
    #create figure
    fig = plt.figure(figsize=(12, 5))
    
    if (Normalize == 1):
        dia = TaylorDiagram(RefStd/RefStd, fig=fig, rect=131, label="Reference")
        dia3 = TaylorDiagram(RefStd/RefStd, fig=fig, rect=132, label="Reference")
        dia4 = TaylorDiagram(RefStd/RefStd, fig=fig, rect=133, label="Reference")
    else:
        dia = TaylorDiagram(RefStd, fig=fig, rect=131, label="Reference")
        dia3 = TaylorDiagram(RefStd, fig=fig, rect=132, label="Reference")
        dia4 = TaylorDiagram(RefStd, fig=fig, rect=133, label="Reference")
        
    # Add grid
    dia.add_grid()
    dia3.add_grid()
    dia4.add_grid()
    
    # Add RMS contours, and label them
    contours = dia.add_contours(colors='0.5')
    PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')
    contours = dia3.add_contours(colors='0.5')
    PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')
    contours = dia4.add_contours(colors='0.5')
    PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')
    
    
    
    # now for each other DEM, calculate the pearson correlation and standard deviation
    
    # for each model run, get all the files and plot them onto the diagram
    markersize = 8
    
    # D1
    files = sorted(glob(DataDirectory+'D1*.txt'))
    n_files = len(files)
    colors = plt.matplotlib.cm.Reds(np.linspace(0.1, 0.9, n_files))
    for i, DEMFileName in enumerate(files):
        pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
        if (Normalize == 1):
            pointsd = pointsd/RefStd
        dia3.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
        if (DEMFileName.endswith('D1-210.txt')):
            dia.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
    
    # D3
    files = sorted(glob(DataDirectory+'D3*.txt'))
    colors = plt.matplotlib.cm.Blues(np.linspace(0.1, 0.9, n_files))
    for i, DEMFileName in enumerate(files):
        pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
        if (Normalize == 1):
            pointsd = pointsd/RefStd
        dia3.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
        if (DEMFileName.endswith('D3-210.txt')):
            dia.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
    
    # D2
    files = sorted(glob(DataDirectory+'D2*.txt'))
    colors = plt.matplotlib.cm.Greens(np.linspace(0.3, 0.7, n_files))
    
    for i, DEMFileName in enumerate(files):
        pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
        if (Normalize == 1):
            pointsd = pointsd/RefStd
        dia4.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
        if (DEMFileName.endswith('D2-210.txt')):
            dia.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
    
    # D4
    files = sorted(glob(DataDirectory+'D4*.txt'))
    colors = plt.matplotlib.cm.Wistia(np.linspace(0.3, 0.7, n_files))
    
    for i, DEMFileName in enumerate(files):
        pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
        if (Normalize == 1):
            pointsd = pointsd/RefStd
        dia4.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
        if (DEMFileName.endswith('D4-210.txt')):
            dia.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])

       
    # add legend
    fig.legend(dia.samplePoints,
               [ p.get_label() for p in dia.samplePoints ],
               numpoints=1, prop=dict(size='small'), loc='center left')
    
    
    plt.savefig(DataDirectory+"fig1.png",format="png",dpi=300)
    
    return fig
    
    
def test2():
    """
    Test 2: Taylor diagram for a single initial condition compared to a single reference case.
    """
    
    # define the FileNames
    DataDirectory = '../Caesar-Ddata/'
    InitialFileName = 'DEM_init.txt'
    RefFileName = 'A1-210.txt'
    
    # parameters
    Normalize = 1
    
    # get the initial DEM
    InitialDEM = ReadInitialDEM(DataDirectory+InitialFileName)
    
    # get the reference DoD and std
    RefDod, RefStd = ReadReference(InitialDEM,DataDirectory+RefFileName)
    #print(RefDod)
    #print(RefStd)
    
    
    #create figure
    fig = plt.figure(figsize=(12, 5))
    
    if (Normalize == 1):
        dia = TaylorDiagram(RefStd/RefStd, fig=fig, rect=131, label="Reference")
        dia3 = TaylorDiagram(RefStd/RefStd, fig=fig, rect=132, label="Reference")
        dia4 = TaylorDiagram(RefStd/RefStd, fig=fig, rect=133, label="Reference")
    else:
        dia = TaylorDiagram(RefStd, fig=fig, rect=131, label="Reference")
        dia3 = TaylorDiagram(RefStd, fig=fig, rect=132, label="Reference")
        dia4 = TaylorDiagram(RefStd, fig=fig, rect=133, label="Reference")
        
    # Add grid
    dia.add_grid()
    dia3.add_grid()
    dia4.add_grid()
    
    # Add RMS contours, and label them
    contours = dia.add_contours(colors='0.5')
    PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')
    contours = dia3.add_contours(colors='0.5')
    PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')
    contours = dia4.add_contours(colors='0.5')
    PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')
    
    
    
    # now for each other DEM, calculate the pearson correlation and standard deviation
    
    # for each model run, get all the files and plot them onto the diagram
    markersize = 8
    
    # D1
    files = sorted(glob(DataDirectory+'D1*.txt'))
    n_files = len(files)
    colors = plt.matplotlib.cm.Reds(np.linspace(0.1, 0.9, n_files))
    for i, DEMFileName in enumerate(files):
        pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
        if (Normalize == 1):
            pointsd = pointsd/RefStd
        dia3.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
        if (DEMFileName.endswith('D1-210.txt')):
            dia.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
    
    # D3
    files = sorted(glob(DataDirectory+'D3*.txt'))
    colors = plt.matplotlib.cm.Blues(np.linspace(0.1, 0.9, n_files))
    for i, DEMFileName in enumerate(files):
        pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
        if (Normalize == 1):
            pointsd = pointsd/RefStd
        dia3.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
        if (DEMFileName.endswith('D3-210.txt')):
            dia.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
    
    # D2
    files = sorted(glob(DataDirectory+'D2*.txt'))
    colors = plt.matplotlib.cm.Greens(np.linspace(0.3, 0.7, n_files))
    
    for i, DEMFileName in enumerate(files):
        pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
        if (Normalize == 1):
            pointsd = pointsd/RefStd
        dia4.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
        if (DEMFileName.endswith('D2-210.txt')):
            dia.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
    
    # D4
    files = sorted(glob(DataDirectory+'D4*.txt'))
    colors = plt.matplotlib.cm.Wistia(np.linspace(0.3, 0.7, n_files))
    
    for i, DEMFileName in enumerate(files):
        pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
        if (Normalize == 1):
            pointsd = pointsd/RefStd
        dia4.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
        if (DEMFileName.endswith('D4-210.txt')):
            dia.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])

       
    # add legend
    fig.legend(dia.samplePoints,
               [ p.get_label() for p in dia.samplePoints ],
               numpoints=1, prop=dict(size='small'), loc='center left')
    
    
    plt.savefig(DataDirectory+"fig1.png",format="png",dpi=300)
    
    return fig
    
    
if __name__ == '__main__':

    test1()
    test2()

    plt.show()
