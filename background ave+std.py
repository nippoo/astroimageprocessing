import numpy as np
import pyfits       # PyFITS at https://pythonhosted.org/pyfits
import matplotlib.pyplot as plt
from pyfits import getheader


import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

hdudata = pyfits.open('mosaic.fits') # we hardcode the input data file
img = hdudata[0].data # img is a NumPy array with the data
mask = np.ones(img.shape, dtype='bool') # create mask with the same dimensions. We set the bit low to mask it

#header = getheader('mosaic.fits')
#print header

masked=img
imgave = np.average(masked)
imgstd = np.std(masked)
print "Initial Average and std deviate:"
print imgave
print imgstd
test=1	
while (test !=0):


	xmax=img.shape[0]
	ymax=img.shape[1]
	for y in range(0,ymax):
		for x in range(0, xmax):
			if img[x,y]>5*imgstd+imgave:
				mask[x,y]= 0
				#print "Setting Zero"

	masked=img*mask
	imgave = np.average(masked)
	imgstd = np.std(masked)
	print "Revised average and std deviation:"
	print imgave
	print imgstd
	test=input("Do you wish to continue (1/0)?")
plt.clf()
plt.imshow(masked)
plt.show()		