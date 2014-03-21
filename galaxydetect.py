import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

# finds galaxies and stores the corresponding data in the catalogue.

s = StarProcessor()


s.mask = np.load("maskfile.npy")	#load the premask
s.RecalculateMasked

stars = [] # intialise catalogue

#galaxy detection
x = 0
while x<500:
	
	starloc = s.FindBrightest()
	if s.img[starloc]<3500:
		print "hit background level in count"
		break
	galcount=s.MaskGalaxy(starloc)
	stars.append({'coords':starloc, 'count':galcount})	#adds star's paramters to catalogue
	print x, "	", galcount
	x=x+1
	
#print stars


plt.clf()
plt.imshow(s.mask)
plt.show()

plt.clf()
plt.imshow(s.masked)
plt.show()



s.RecalculateMasked
fluxlist = [i['count'] for i in stars]
values, base = np.histogram(fluxlist, bins=40)
cumulative = np.cumsum(values)
plt.plot(base[:-1], cumulative, c='blue')
 
plt.show()