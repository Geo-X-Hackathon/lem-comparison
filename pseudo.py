# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def ReadReference(initDEM,refDEM,refDOD,refsd)
    read initDEM
    read refDEM
    refDOD = refDEM-initDEM
    refsd = standard_deviation(refDOD)



def AddTaylorDEM(DEM,refDOD,colour):
    read DEM
    DOD = DEM-refDEM
    sd = standard_deviaton(DOD)
    cp = pearson_correlation(DOD,refDOD)
  