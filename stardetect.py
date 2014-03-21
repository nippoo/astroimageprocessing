import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

s = StarProcessor()

stars = []
x=0
while x<20:
	starloc = s.FindBrightest()
	print s.img[starloc]
	if s.img[starloc] < 34000: # we say this isn't a star any more - 2sd above background
		print "break"
		break
	s.MaskStar(starloc) # this is a new star, add it to our dict
	x=x+1
	print x

        
s.RecalculateMasked
# fluxlist = [i['count'] for i in stars]
# values, base = np.histogram(fluxlist, bins=40)
# cumulative = np.cumsum(values)
# plt.plot(base[:-1], cumulative, c='blue')
# 
# plt.show()

plt.clf()
plt.imshow(s.mask)
plt.show()

plt.clf()
plt.imshow(s.masked)
plt.show()