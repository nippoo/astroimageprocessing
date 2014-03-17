import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path



s = StarProcessor()



plt.clf()
plt.imshow(s.img)
plt.show()


# Code to plot histogram of intensity. Optional log scale. 

fig, ax = plt.subplots()

# histogram our data with numpy

n, bins = np.histogram(s.img, 10000)	# indjusts the numbe of bins.

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
patch = patches.PathPatch(barpath, facecolor='blue', edgecolor='blue', alpha=0.8)
ax.add_patch(patch)

# update the view limits
ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())
ax.set_yscale('log')					#sets log scale for y-axis
plt.show()