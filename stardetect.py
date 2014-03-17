import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

s = StarProcessor()

stars = []
x=0
while x<2000:
    starloc = s.FindBrightest()
    if s.MaskStar(starloc): # this is a new star, add it to our dict
        flux = s.flux(starloc)	#calculates the Flux from the count for the star
        stars.append({'coords':starloc, 'count':s.img[starloc], 'flux':flux})	#adds star's paramters to catalogue
        print "Star", x, "found with count", s.img[starloc]
        x=x+1
    if s.img[starloc] < 3500: # we say this isn't a star any more - 2sd above background
        break
        
countlist = [i['count'] for i in stars]
fluxlist = [i['flux'] for i in stars]
values, base = np.histogram(fluxlist, bins=40)
cumulative = np.cumsum(values)
plt.plot(base[:-1], cumulative, c='blue')

plt.show()

plt.clf()
plt.imshow(s.masked)
plt.show()