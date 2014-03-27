import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

import csv

# finds galaxies and stores the corresponding data in the catalogue.

s = StarProcessor()


s.mask = np.load("maskfile.npy")	#load the premask
s.RecalculateMasked()

stars = [] # intialise catalogue

#galaxy detection
x = 0
while x<1000:
	
    starloc = s.FindBrightest()
    if s.img[starloc]<3500:
    	print "hit background level in count"
    	break
    galradius=s.FindGalaxyRadius(starloc)
    #galradius = 12
    galcount, galerror=s.MaskGalaxy(starloc, Gradius=galradius, inner_Bradius = galradius + 15, Bradius = galradius + 80)
    if galcount>0:
		galflux=s.count_to_flux(galcount)
		galfluxerror=s.count_to_flux_error(galcount,galerror)
		stars.append({'coords':starloc, 'peakcount':s.img[starloc],'avecount':galcount, 'flux':galflux, 'fluxerror':galfluxerror, 'radius':galradius})	#adds star's paramters to catalogue
		print x,"	", galcount, "	", galflux,  "	", galradius, "	", galfluxerror
		x=x+1
#print stars

s.RecalculateMasked
np.save("catalogue", stars)
with open('starcatalogue.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Co-ord','Peak-Count','Average-Count', 'Average-Flux', 'Error-in-Flux', 'Radius',)
    for i in stars:
        spamwriter.writerow([i['coords'][0], i['coords'][1],i['peakcount'],i['avecount'], i['flux'], i['fluxerror'], i['radius']])
        
plt.clf()
plt.imshow(s.mask)
plt.show()

plt.clf()
plt.imshow(s.masked)
plt.show()
