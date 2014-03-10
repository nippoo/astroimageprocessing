import numpy as np
import pyfits       # PyFITS at https://pythonhosted.org/pyfits

hdudata = pyfits.open('mosaic.fits') # we hardcode the input data file
img = hdudata[0].data # img is a NumPy array with the data
mask = np.ones(img.shape, dtype='bool') # create mask with the same dimensions. We set the bit low to mask it

print img