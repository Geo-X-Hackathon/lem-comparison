#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:21:06 2018

@author: armitage
"""

import gdalio as gdal_io
import numpy as np
from differences import *
from correlation import *

def input_caesar1(DataDirectory,InitialFileName,Filename_TS1,Filename_TS2):
    print ("Reading in the raster data...")

    # these are np.arrays with the raster data
    InitialTopoArray = gdal_io.ReadRasterArrayBlocks(DataDirectory+InitialFileName,raster_band=1)
    TimeStep1Array = gdal_io.ReadRasterArrayBlocks(DataDirectory+Filename_TS1,raster_band=1)
    TimeStep2Array = gdal_io.ReadRasterArrayBlocks(DataDirectory+Filename_TS2,raster_band=1)

    # strip the nans
    InitialTopoArray = InitialTopoArray[np.logical_not(np.isnan(InitialTopoArray))]
    TimeStep1Array = TimeStep1Array[np.logical_not(np.isnan(TimeStep1Array))]
    TimeStep2Array = TimeStep2Array[np.logical_not(np.isnan(TimeStep2Array))]

    return (InitialTopoArray, TimeStep1Array, TimeStep2Array)

def ReadInitialDEM(InitialFileName):
    """
    Function to read in the initial DEM and return it
    """
    # read in the DEMs
    InitialDEM = gdal_io.ReadRasterArrayBlocks(InitialFileName,raster_band=1)
    return InitialTopoArray

def ReadReference(InitialDEM, RefFileName):
    """
    Function to read in the reference DEM and return the reference DEM of difference and the standard deviation
    """
    RefDEM = gdal_io.ReadRasterArrayBlocks(RefFileName,raster_band=1)

    # get the reference DOD
    RefDoD = dem_difference(RefDEM - InitialDEM)

    # get the standard deviation of the reference DOD
    std = standard_deviation(RefDoD)

    return RefDoD, std

def CalculateTaylorPoint(DEMFileName, InitialDEM, RefDoD):
    """
    Function to read in a DEM, calculate the DEM of difference and return the Pearson correlation and standard deviation compared to the reference DEM of difference
    """
    ThisDEM = gdal_io.ReadRasterArrayBlocks(DEMFileName,raster_band=1)

    #get the DOD
    ThisDoD = dem_difference(ThisDEM - Initial_DEM)

    # get the pearson correlation and std compared to the reference DoD
    ThisR = pearson_correlation(RefDoD, ThisDoD)
    ThisStd = standard_deviation(ThisDoD)

    return ThisR, ThisStd
