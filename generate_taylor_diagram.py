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

def SetUpTaylorDiagram(DataDirectory, RefFileName, InitialDEM, RefStd, Normalize=0):
    """
    Set up the taylor diagram using the intiial DEM and the
    reference DEM
    """

    #create figure
    fig = plt.figure(figsize=(10, 10))

    if (Normalize == 1):
        dia = TaylorDiagram(RefStd/RefStd, fig=fig, rect=111, label="Reference")
    else:
        dia = TaylorDiagram(RefStd, fig=fig, rect=111, label="Reference")

    # Add grid
    dia.add_grid()

    # Add RMS contours, and label them
    contours = dia.add_contours(colors='0.5')
    PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')

    return fig, dia

def AddSinglePointToDiagram(DataDirectory,DEMFileName, InitialDEM, RefDod, Normalize=0, color='k', label=' ', markersize=8):
    """
    Function to add a point from a single DEM to the diagram
    """
    # check if you want to label the point
    this_label = DEMFileName
    if label != ' ':
        this_label = label

    pointcp, pointsd = CalculateTaylorPoint(DataDirectory+DEMFileName,InitialDEM,RefDod)
    if (Normalize == 1):
        pointsd = pointsd/RefStd
    dia.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=color, mec='k', label=this_label)


if __name__ == '__main__':

    # declare the parameters
    DataDirectory = '../MuddPILE_data/'
    InitialFileName = 'Initial_topography.bil'
    RefFileName = 'Reference_TS60.bil'
    Normalize = 1

    # read the initial DEM
    InitialDEM = ReadInitialDEM(DataDirectory+InitialFileName)
    # read the reference DEM
    RefDod, RefStd = ReadReference(InitialDEM,DataDirectory+RefFileName)

    # set up the Taylor Diagram
    fig, dia = SetUpTaylorDiagram(DataDirectory, RefFileName, InitialDEM, RefStd, Normalize)

    # proof of concept - just add one point to the diagram
    DEMFileName = 'movern_0p35_n_is_two60.bil'
    color = 'blue'
    # now add a point
    AddSinglePointToDiagram(DataDirectory,DEMFileName, InitialDEM, RefDod, Normalize, color)

    # add legend
    fig.legend(dia.samplePoints,
               [ p.get_label() for p in dia.samplePoints ],
               numpoints=1, prop=dict(size='medium'), loc='upper right')


    plt.tight_layout()
    plt.savefig(DataDirectory+"taylor_diagram.png",format="png",dpi=300)
