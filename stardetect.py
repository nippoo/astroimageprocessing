import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

s = StarProcessor()

stars = []
x=0
while x<1000:
    starloc = s.FindBrightest()
    if s.MaskStar(starloc): # this is a new star, add it to our dict
        stars.append({'coords':starloc, 'flux':s.img[starloc]})	#adds star's paramters to catalogue
        print "Star", x, "found with flux", s.img[starloc]
        x=x+1
    if s.img[starloc] < 3500: # we say this isn't a star any more - 2sd above background
        break
        
fluxlist = [i['flux'] for i in stars]
values, base = np.histogram(fluxlist, bins=40)
cumulative = np.cumsum(values)
plt.plot(base[:-1], cumulative, c='blue')

plt.show()

plt.clf()
plt.imshow(s.masked)
plt.show()