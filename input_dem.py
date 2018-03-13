#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:21:06 2018

@author: armitage
"""

import gdalio as gdal_io
import numpy as np

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
