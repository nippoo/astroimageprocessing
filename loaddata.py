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

#img = [(np.sign(x-9000.0)) for x in img]
#img = [x - 3419.0 for x in img]
#plt.clf()
#plt.imshow(img)
#plt.show()

masked=img

test=1	
while (test !=0):
	imgave = np.average(masked)
	imgstd = np.std(masked)
	print imgave
	print imgstd

	xmax=img.shape[0]
	ymax=img.shape[1]
	for y in range(0,ymax):
		for x in range(0, xmax):
			if img[x,y]>4*imgstd+imgave:
				mask[x,y]= 0
				#print "Setting Zero"

	masked=img*mask
	
	test=input("Do you wish to continue (1/0)?")
plt.clf()
plt.imshow(masked)
plt.show()		
"""

# Code to plot histogram of intensity. Optional log scale. 

fig, ax = plt.subplots()

# histogram our data with numpy

n, bins = np.histogram(masked, 10000)	# indjusts the numbe of bins.

# get the corners of the rectangles for the histogram
left = np.array(bins[:-1])
right = np.array(bins[1:])
bottom = np.zeros(len(left))
top = bottom + n


# we need a (numrects x numsides x 2) numpy array for the path helper
# function to build a compound path
XY = np.array([[left,left,right,right], [bottom,top,top,bottom]]).T

# get the Path object
barpath = path.Path.make_compound_path_from_polys(XY)

# make a patch out of it
patch = patches.PathPatch(barpath, facecolor='blue', edgecolor='gray', alpha=0.8)
ax.add_patch(patch)

# update the view limits
ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())
ax.set_yscale('log')					#sets log scale for y-axis
plt.show()

"""