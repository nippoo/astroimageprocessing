import numpy as np
import pyfits       # PyFITS at https://pythonhosted.org/pyfits

# Easier to hardcode the file, since we're working with a single file for the moment
filename = 'mosaic.fits'

class StarProcessor:
    def __init__(self):
        self.OpenFile()
        
    def OpenFile(self):    
        self.hdudata = pyfits.open(filename) # we hardcode the input data file
        self.img = self.hdudata[0].data # img is a NumPy array with the data
        self.mask = np.ones(self.img.shape, dtype='bool') # create mask with the same dimensions. We set the bit low to mask it
        
        self.RecalculateMasked()

    def FindBrightest(self):
        # Finds the brightest unmasked pixel in an image and returns a tuple with its coordinates.
        return np.unravel_index(np.argmax(self.masked), self.img.shape)
    
    def MaskStar(self, coords, radius=20):
        # Masks star based on given pixel value, and returns a mask
		for y in range(-radius+1,radius):
			for x in range(-radius+1,+radius):
				if (x**2+y**2)<radius**2:
					self.mask[coords[0]+x,coords[1]+y] = 0
    def RecalculateMasked(self):
        self.masked = self.img*self.mask