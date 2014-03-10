import numpy as np
import pyfits       # PyFITS at https://pythonhosted.org/pyfits

hdudata = pyfits.open('mosaic.fits') # we hardcode the input data file
img = hdudata[0].data # img is a NumPy array with the data

print img.shape