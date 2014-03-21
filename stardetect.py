import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

s = StarProcessor()



stars = []


#pre-masking
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

plt.clf()
plt.imshow(s.mask)
plt.show()

plt.clf()
plt.imshow(s.masked)
plt.show()


#galaxy detection
x = 0
while x<10:
	print x
	starloc = s.FindBrightest()
	if s.img[starloc]<3500:
		break
	galcount=s.MaskGalaxy(starloc)
	stars.append({'coords':starloc, 'ave count':galcount})	#adds star's paramters to catalogue
	x=x+1
	
print stars

plt.clf()
plt.imshow(s.mask)
plt.show()

plt.clf()
plt.imshow(s.masked)
plt.show()



s.RecalculateMasked
# fluxlist = [i['count'] for i in stars]
# values, base = np.histogram(fluxlist, bins=40)
# cumulative = np.cumsum(values)
# plt.plot(base[:-1], cumulative, c='blue')
# 
# plt.show()