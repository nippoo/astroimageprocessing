import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

from starfinder import StarFinder

s = StarFinder()

StarFinder.OpenFile(s)

print s.img

#header = pyfits.getheader('mosaic.fits')
#print header

#img = [(np.sign(x-9000.0)) for x in img]
#img = [x - 3419.0 for x in img]
#plt.clf()
#plt.imshow(img)
#plt.show()

