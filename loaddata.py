import numpy as np
import pyfits       # PyFITS at https://pythonhosted.org/pyfits
import matplotlib.pyplot as plt

hdudata = pyfits.open('mosaic.fits') # we hardcode the input data file
img = hdudata[0].data # img is a NumPy array with the data
mask = np.ones(img.shape, dtype='bool') # create mask with the same dimensions. We set the bit low to mask it

img = [(np.sign(x-3420.0)) for x in img]
plt.clf()
plt.imshow(img)
plt.show()

# for i in img:
#     for j in i:
#         if j < 3419.0:
#             x.push(i)