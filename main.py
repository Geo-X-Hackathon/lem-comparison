# Script to make a Taylor diagram from LEM inputs
# Geo.X hackathon 13/03/18

import gdal-io

# read in the raster
DataDirectory = 'path/to/data/directory/'
RasterName = 'initial_topography.asc'

# this is a np.array with the raster data
RasterData = gdal-io.ReadRasterArrayBlocks(raster_file,raster_band=1)
