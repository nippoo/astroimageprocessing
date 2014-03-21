import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

s = StarProcessor()

# Finds the brightest stella objects and generates a mask coresponding to their location which
# is then saved to "maskfile".

#pre-masking
x=0
print "Finding Galaxies"
while x<20:
	starloc = s.FindBrightest()
	print s.img[starloc]
	if s.img[starloc] < 34000: # we say this isn't a star any more
		print "break"
		break
	s.MaskStar(starloc) 
	x=x+1
	#print x
np.save("maskfile", s.mask)

plt.clf()
plt.imshow(s.mask)
plt.show()

plt.clf()
plt.imshow(s.masked)
plt.show()