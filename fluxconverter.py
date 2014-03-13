def fluxconv(count):		#converts the count reading into flux using the predefined MAGZPT value.

	flux = -2.5*np.log10(count)
	flux = flux + MAGZPT
	return flux


import numpy as np
import pyfits       # PyFITS at https://pythonhosted.org/pyfits
import matplotlib.pyplot as plt
from pyfits import getheader

#Fetch Values stored in Header of FITS image
header = getheader('mosaic.fits')
MAGZPT = header['MAGZPT']
#MAGZRR = header['MAGZRR']

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

hdudata = pyfits.open('mosaic.fits') # we hardcode the input data file
img = hdudata[0].data # img is a NumPy array with the data

#mask = np.ones(img.shape, dtype='bool') # create mask with the same dimensions. We set the bit low to mask it

imgflux=np.zeros(img.shape)

xmax=img.shape[0]
ymax=img.shape[1]

for y in range(0,ymax):
	for x in range(0, xmax):
		imgflux[x,y] = fluxconv(img[x,y])

plt.clf()
plt.imshow(imgflux)
plt.show()



