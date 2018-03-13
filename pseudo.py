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



def CalculateTaylorPoint(DEM,initDEM,refDOD,sd,cp):
    read DEM
    DOD = DEM-initDEM
    sd = standard_deviaton(DOD)
    cp = pearson_correlation(DOD,refDOD)
    



----

ReadReference("DEM_init.txt","A1-210.txt",refDOD,refsd)

#create figure
fig = PLT.figure(figsize=(10, 4))
dia = TaylorDiagram(refsd, fig=fig, rect=122, label="Reference")

# Add grid
dia.add_grid()

# Add RMS contours, and label them
contours = dia.add_contours(colors='0.5')
PLT.clabel(contours, inline=1, fontsize=10, fmt='%.2f')



CalculateTaylorPoint("D1-210.txt",refDOD,pointsd,pointcp)
dia.add_sample(pointsd, pointcp, marker='o', ms=6, ls='', mfc='k', mec='k')

