import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

# finds galaxies and stores the corresponding data in the catalogue.

s = StarProcessor()


s.mask = np.load("maskfile.npy")	#load the premask
s.RecalculateMasked()

stars = [] # intialise catalogue

#galaxy detection
x = 0
while x<500:
	
    starloc = s.FindBrightest()
    if s.img[starloc]<3500:
    	print "hit background level in count"
    	break
    galradius=s.FindGalaxyRadius(starloc)
    galcount=s.MaskGalaxy(starloc, Gradius=galradius, inner_Bradius = galradius + 15, Bradius = galradius + 80)
    if galcount>0:
		galflux=s.count_to_flux(galcount)
		stars.append({'coords':starloc, 'count':galcount, 'flux':galflux})	#adds star's paramters to catalogue
		print x,"	", starloc, "	",s.img[starloc],"	", galcount,  "	", galflux,  "	", galradius
		x=x+1
#print stars


plt.clf()
plt.imshow(s.mask)
plt.show()

plt.clf()
plt.imshow(s.masked)
plt.show()

s.RecalculateMasked
np.save("catalogue", stars)
fluxlist = [i['flux'] for i in stars]
values, base = np.histogram(fluxlist, bins=40)
cumulative = np.cumsum(values)
plt.plot(base[:-1], cumulative, c='blue')
plt.semilogy()
#ax = plt
#ax.set_yscale('log') 
plt.show()
