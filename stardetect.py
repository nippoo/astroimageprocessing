import numpy as np
from starprocessor import StarProcessor

s = StarProcessor()

stars = []

for x in range(0, 10):
    starloc = s.FindBrightest()
    if s.MaskStar(starloc): # this is a new star, add it to our dict
         stars.append({'coords':starloc, 'mag':s.img[starloc]})
         
print stars