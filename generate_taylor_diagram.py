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
import os

def SetUpTaylorDiagram(RefStd, Normalize=0, figsize=(10,10)):
    """
    Set up the taylor diagram using the intiial DEM and the
    reference DEM

    Args:
        RefStd (float): the standard deviation of the reference DoD
        Normalize (int): a switch to choose whether or not to noramlise the standard
        deviation. 0 = don't noramlise (default); 1 = normalise.
    """

    #create figure
    fig = plt.figure(figsize=figsize)

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

def AddSinglePointToDiagram(DataDirectory,DEMFileName, InitialDEM, RefDod, RefStd, Normalize=0, color='k', label=' ', markersize=8):
    """
    Function to add a point from a single DEM to the diagram

    Args:
        DataDirectory (str): the name of the data directory
        DEMFileName (str): name of the DEM that you want to plot
        InitialDEM (arr): array of the initial DEM
        RefDod (arr): array with the DEM of difference for the reference DEM
        RefStd (float): the standard deviation of the reference DoD
        Normalize (int): a switch to choose whether or not to noramlise the standard
        deviation. 0 = don't noramlise (default); 1 = normalise.
        color (str): the color that you want the point to be, default = black
        label (str): you can pass a string to the legend for the label. If not passed, then it will just be labelled with the name of the DEM.
        markersize (int): size of the point
    """
    # check if you want to label the point
    this_label = DEMFileName
    if label != ' ':
        this_label = label

    pointcp, pointsd = CalculateTaylorPoint(DataDirectory+DEMFileName,InitialDEM,RefDod)
    if (Normalize == 1):
        pointsd = pointsd/RefStd
    dia.add_sample(pointsd, pointcp, marker='o', ms=markersize, ls='', mfc=color, mec='k', label=this_label)

def AddTimeSeriesToDiagram(DataDirectory, SubDirectory, FilenamePrefix, DEM_extension, InitialDEM, RefDod, RefStd, Normalize=0, colormap= plt.matplotlib.cm.viridis, label=' ', markersize=8, markerstyle='o'):
    """
    Function to add a time series of model runs to the diagram.  The time series should be in its own
    sub-directory.
    Ideally the DEMs need to have the format:
        FilenamePrefix_XXX.extension

    where XXX is the number.  Files will be read in ascending order (through time)

    Args:
        DataDirectory (str): the name of the data directory
        SubDirectory (str): name of the subdirectory with the time series DEMs
        FilenamePrefix (str): a standardised string for the start of the filename.
        DEM_extension (str): a string with the extension of the DEM, e.g. "txt", "asc", or "bil"
        InitialDEM (arr): array of the initial DEM
        RefDod (arr): array with the DEM of difference for the reference DEM
        RefStd (float): the standard deviation of the reference DoD
        Normalize (int): a switch to choose whether or not to noramlise the standard
        deviation. 0 = don't noramlise (default); 1 = normalise.
        colormap (str): colormap for the points, default = viridis
        label (list): you can pass a list to the legend for the labels. If not passed, then it will just be labelled with the name of each DEM.
        markersize (int): size of the point
        markerstyle (str): style of the marker, default = circle.
    """

    # read in the files in the specified directory
    files = sorted(glob(DataDirectory+SubDirectory+FilenamePrefix+'*'+DEM_extension))
    print files
    n_files = len(files)
    colors = colormap(np.linspace(0.1, 0.9, n_files))

    # loop through and add each point to the diagram
    for i, DEMFileName in enumerate(files):
        # split the filename to just get that of the DEM
        # first check the operating system - will be different if windows
        path, file = os.path.split(DEMFileName)
        file = file.split('.')[0]
        # check if you want to specify your own labels
        this_label = file
        if label != ' ':
            this_label = label[i]

        pointcp, pointsd = CalculateTaylorPoint(DEMFileName,InitialDEM,RefDod)
        if (Normalize == 1):
            pointsd = pointsd/RefStd
        dia.add_sample(pointsd, pointcp, marker=markerstyle, ms=markersize, ls='', mfc=colors[i], mec='k', label=this_label)

if __name__ == '__main__':

    # declare the parameters
    DataDirectory = '../Caesar-Ddata/'
    InitialFileName = 'DEM_init.txt'
    RefFileName = 'A1-210.txt'
    Normalize = 1

    # read the initial DEM
    InitialDEM = ReadInitialDEM(DataDirectory+InitialFileName)
    # read the reference DEM
    RefDod, RefStd = ReadReference(InitialDEM,DataDirectory+RefFileName)

    # set up the Taylor Diagram
    figsize = (6,5) # the figure size in inches (width, height)
    fig, dia = SetUpTaylorDiagram(RefStd, Normalize, figsize)

    # proof of concept - make a time series
    SubDir = 'D1/'
    FilenamePrefix = 'D1'
    colormap =  plt.matplotlib.cm.Reds
    AddTimeSeriesToDiagram(DataDirectory,SubDir,FilenamePrefix,'txt',InitialDEM,RefDod,RefStd,Normalize,colormap)

    # now add another one just for fun
    SubDir = 'D3/'
    FilenamePrefix = 'D3'
    colormap = plt.matplotlib.cm.Blues
    AddTimeSeriesToDiagram(DataDirectory,SubDir,FilenamePrefix,'txt',InitialDEM,RefDod,RefStd,Normalize,colormap)

    # add legend
    fig.legend(dia.samplePoints,
               [ p.get_label() for p in dia.samplePoints ],
               numpoints=1, prop=dict(size='medium'), loc='upper right')


    plt.subplots_adjust(left=0.05) # just some figure adjustment to allow space for legend
    # save the figure
    plt.savefig(DataDirectory"taylor_diagram_time_series.png",format="png",dpi=300)
