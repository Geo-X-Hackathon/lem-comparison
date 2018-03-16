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
    # parameters
    Normalize = 0
    markersize = 8
    markerstyle = 'o'

    
    # define the FileNames
    DataDirectory = '../Caesar-Ddata/'
    InitialFileName = 'DEM_init.txt'
    RefFileName = 'A1-210.txt'
    
    
    # get the initial DEM
    InitialDEM = ReadInitialDEM(DataDirectory+InitialFileName)
    
    # get the reference DoD and std
    RefDod, RefStd = ReadReference(InitialDEM,DataDirectory+RefFileName)
    #print(RefDod)
    #print(RefStd)
    
    
    #create figure
    fig = plt.figure(figsize=(7, 5))
    
    if (Normalize == 1):
        dia = TaylorDiagram(RefStd/RefStd, fig=fig, rect=111, label="Reference")
    else:
        dia = TaylorDiagram(RefStd, fig=fig, rect=111, label="Reference")
        
    # Add grid
    dia.add_grid()
    
    # Add RMS contours, and label them
    contours = dia.add_contours(colors='0.5')
    PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')
    
    
    
    # now for each other DEM, calculate the pearson correlation and standard deviation
    
    # for each model run, get all the files and plot them onto the diagram
    
    # D1
    color = plt.matplotlib.cm.Reds(0.9)
    DEMFileName = DataDirectory+'D1-210.txt'
    pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
    if (Normalize == 1):
        pointsd = pointsd/RefStd
    dia.add_sample(pointsd, pointcp, marker=markerstyle, ms=markersize, ls='', mfc=color, mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
    
    # D2
    color = plt.matplotlib.cm.Greens(0.9)
    DEMFileName = DataDirectory+'D2-210.txt'
    pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
    if (Normalize == 1):
        pointsd = pointsd/RefStd
    dia.add_sample(pointsd, pointcp, marker=markerstyle, ms=markersize, ls='', mfc=color, mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])

    # D3
    color = plt.matplotlib.cm.Blues(0.9)
    DEMFileName = DataDirectory+'D3-210.txt'
    pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
    if (Normalize == 1):
        pointsd = pointsd/RefStd
    dia.add_sample(pointsd, pointcp, marker=markerstyle, ms=markersize, ls='', mfc=color, mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
    
    # D3
    color = plt.matplotlib.cm.spring(0.9)
    DEMFileName = DataDirectory+'D4-210.txt'
    pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
    if (Normalize == 1):
        pointsd = pointsd/RefStd
    dia.add_sample(pointsd, pointcp, marker=markerstyle, ms=markersize, ls='', mfc=color, mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])

       
    # add legend
    fig.legend(dia.samplePoints,
               [ p.get_label() for p in dia.samplePoints ],
               numpoints=1, prop=dict(size='small'), loc='center left')
    
    
    plt.savefig(DataDirectory+"fig1.png",format="png",dpi=300)
    
    return fig


def test2():
    """
    Test 2: Taylor diagram for a time series compared to a single reference case.
    """
    
    # define the FileNames
    DataDirectory = '../Caesar-Ddata/'
    InitialFileName = 'DEM_init.txt'
    RefFileName = 'A1-210.txt'
    
    # parameters
    Normalize = 0
    markersize = 8
    markerstyle = 'o'
    
    # get the initial DEM
    InitialDEM = ReadInitialDEM(DataDirectory+InitialFileName)
    
    # get the reference DoD and std
    RefDod, RefStd = ReadReference(InitialDEM,DataDirectory+RefFileName)
    #print(RefDod)
    #print(RefStd)
    
    
    #create figure
    fig = plt.figure(figsize=(12, 5))
    
    if (Normalize == 1):
        dia1 = TaylorDiagram(RefStd/RefStd, fig=fig, rect=121, label="Reference")
        dia2 = TaylorDiagram(RefStd/RefStd, fig=fig, rect=122, label="Reference")
    else:
        dia1 = TaylorDiagram(RefStd, fig=fig, rect=121, label="Reference")
        dia2 = TaylorDiagram(RefStd, fig=fig, rect=122, label="Reference")
        
    # Add grid
    dia1.add_grid()
    dia2.add_grid()
    
    # Add RMS contours, and label them
    #contours = dia.add_contours(colors='0.5')
    #PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')
    contours = dia1.add_contours(colors='0.5')
    PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')
    contours = dia2.add_contours(colors='0.5')
    PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')
    
    
    
    # now for each other DEM, calculate the pearson correlation and standard deviation
    
    # for each model run, get all the files and plot them onto the diagram
    # D1
    files = sorted(glob(DataDirectory+'D1*.txt'))
    n_files = len(files)
    colors = plt.matplotlib.cm.Reds(np.linspace(0.1, 0.9, n_files))
    for i, DEMFileName in enumerate(files):
        pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
        if (Normalize == 1):
            pointsd = pointsd/RefStd
        dia1.add_sample(pointsd, pointcp, marker=markerstyle, ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
    
    # D3
    files = sorted(glob(DataDirectory+'D3*.txt'))
    colors = plt.matplotlib.cm.Blues(np.linspace(0.1, 0.9, n_files))
    for i, DEMFileName in enumerate(files):
        pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
        if (Normalize == 1):
            pointsd = pointsd/RefStd
        dia1.add_sample(pointsd, pointcp, marker=markerstyle, ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
    
    # D2
    files = sorted(glob(DataDirectory+'D2*.txt'))
    colors = plt.matplotlib.cm.Greens(np.linspace(0.3, 0.7, n_files))
    
    for i, DEMFileName in enumerate(files):
        pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
        if (Normalize == 1):
            pointsd = pointsd/RefStd
        dia2.add_sample(pointsd, pointcp, marker=markerstyle, ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
    
    # D4
    files = sorted(glob(DataDirectory+'D4*.txt'))
    colors = plt.matplotlib.cm.spring(np.linspace(0.3, 0.7, n_files))
    
    for i, DEMFileName in enumerate(files):
        pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
        if (Normalize == 1):
            pointsd = pointsd/RefStd
        dia2.add_sample(pointsd, pointcp, marker=markerstyle, ms=markersize, ls='', mfc=colors[i], mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])

       
    # add legend
    fig.legend(dia1.samplePoints,
               [ p.get_label() for p in dia1.samplePoints ],
               numpoints=1, prop=dict(size='small'), loc='center left')
    
    
    plt.savefig(DataDirectory+"fig2.png",format="png",dpi=300)
    
    return fig
    


def test3():
    """
    Test 3: Taylor diagram for a different initial conditions compared to different reference cases.
    """
    # parameters
    Normalize = 1
    markersize = 8
    markerstyle = 'o'

    
    # define the FileNames
    DataDirectory = '../Caesar-Ddata/'
    InitialFileName = 'DEM_init.txt'
    RefFileName = 'A1-210.txt'
    
    
    # get the initial DEM
    InitialDEM = ReadInitialDEM(DataDirectory+InitialFileName)
    
    # get the reference DoD and std
    RefDod, RefStd = ReadReference(InitialDEM,DataDirectory+RefFileName)
    #print(RefDod)
    #print(RefStd)
    
    
    #create figure
    fig = plt.figure(figsize=(7, 5))
    
    if (Normalize == 1):
        dia = TaylorDiagram(RefStd/RefStd, fig=fig, rect=111, label="Reference")
    else:
        dia = TaylorDiagram(RefStd, fig=fig, rect=111, label="Reference")
        
    # Add grid
    dia.add_grid()
    
    # Add RMS contours, and label them
    contours = dia.add_contours(colors='0.5')
    PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')
    
    
    
    # now for each other DEM, calculate the pearson correlation and standard deviation
    
    # for each model run, get all the files and plot them onto the diagram
    
    # D1
    color = plt.matplotlib.cm.Reds(0.9)
    DEMFileName = DataDirectory+'D1-210.txt'
    pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
    if (Normalize == 1):
        pointsd = pointsd/RefStd
    dia.add_sample(pointsd, pointcp, marker=markerstyle, ms=markersize, ls='', mfc=color, mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])
    
    # D2
    color = plt.matplotlib.cm.Greens(0.9)
    DEMFileName = DataDirectory+'D2-210.txt'
    pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
    if (Normalize == 1):
        pointsd = pointsd/RefStd
    dia.add_sample(pointsd, pointcp, marker=markerstyle, ms=markersize, ls='', mfc=color, mec='k', label=DEMFileName[len(DataDirectory):len(DEMFileName)-4])


    # now the other ones
    markerstyle = 's'

    # define the FileNames
    DataDirectory = '../MuddPILE_data/'
    InitialFileName = 'Initial_topography.bil'
    RefFileName = 'Reference_TS60.bil'

    # get the initial DEM
    InitialDEM = ReadInitialDEM(DataDirectory+InitialFileName)
    
    # get the reference DoD and std
    RefDod, RefStd = ReadReference(InitialDEM,DataDirectory+RefFileName)
    
    # n = 1.5
    color = plt.matplotlib.cm.spring(0.9)
    DEMFileName = DataDirectory+'movern_0p35_n_is_one_and_half60.bil'
    pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
    if (Normalize == 1):
        pointsd = pointsd/RefStd
    dia.add_sample(pointsd, pointcp, marker=markerstyle, ms=markersize, ls='', mfc=color, mec='k', label='MUDD n=1.5')
    
    # n = 2.0
    color = plt.matplotlib.cm.Blues(0.9)
    DEMFileName = DataDirectory+'movern_0p35_n_is_two60.bil'
    pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
    if (Normalize == 1):
        pointsd = pointsd/RefStd
    dia.add_sample(pointsd, pointcp, marker=markerstyle, ms=markersize, ls='', mfc=color, mec='k', label='MUDD n=2.0')




       
    # add legend
    fig.legend(dia.samplePoints,
               [ p.get_label() for p in dia.samplePoints ],
               numpoints=1, prop=dict(size='small'), loc='center left')
    
    
    plt.savefig(DataDirectory+"fig3.png",format="png",dpi=300)
    
    return fig
    
        
    
if __name__ == '__main__':

    test1()
    test2()
    test3()

    plt.show()
