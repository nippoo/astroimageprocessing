import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

s = StarProcessor()

stars = []

for x in range(0, 500):
    
    starloc = s.FindBrightest()
    if s.MaskStar(starloc): # this is a new star, add it to our dict
        flux = s.flux(starloc)	#calculates the Flux from the count for the star
        stars.append({'coords':starloc, 'count':s.img[starloc], 'flux':flux})	#adds star's paramters to catalogue
        print "Star", x, "found with count", s.img[starloc]
        
    if s.img[starloc] < 4540: # we say this isn't a star any more - 2sd above background
        break
        