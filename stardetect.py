import numpy as np
from starprocessor import StarProcessor

s = StarProcessor()

stars = []

for x in range(0, 10):
    starloc = s.FindBrightest()
    if s.MaskStar(starloc): # this is a new star, add it to our dict
		flux = s.flux(starloc)	#calculates the Flux from the count for the star
		stars.append({'coords':starloc, 'count':s.img[starloc], 'flux':flux})	#adds star's paramters to catalogue
         
print stars