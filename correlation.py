# Function to calculate Pearson correlation and standard deviation

import numpy as np

def pearson_correlation(reference_dem,test_dem):

    r = np.corrcoef(reference_dem,test_dem)[0, 1]
    return r

def standard_deviation(dem):

    std = dem.std(ddof=1)
    return std
