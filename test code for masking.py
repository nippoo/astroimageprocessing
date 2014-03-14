import numpy as np
from starprocessor import StarProcessor
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

s = StarProcessor()
#bright_loc=[0,0]
x=0
while  x<1000:
	bright_loc=s.FindBrightest()
	s.MaskStar(bright_loc)
	print bright_loc
	x=x+1

plt.clf()
plt.imshow(s.masked)
plt.show()
