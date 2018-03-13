# Function to calculate Pearson correlation and standard deviation

import numpy as np

def pearson_correlation_std(reference_dem,test_dem):

    std = test_dem.std(ddof=1)
    r = np.corrcoef(reference_dem,test_dem)[0, 1]

    return r, std
