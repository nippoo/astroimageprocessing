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
        
        self.masked = self.img

    def FindBrightest(image, mask):
        # Finds the brightest unmasked pixel in an image and returns a tuple with its coordinates.
        maskedimg = image * mask
        return np.unravel_index(np.argmax(maskedimg), image.shape)
    
    def MaskStar(image, coords, size=[[12, 12]]):
        pass
        # Masks star based on given pixel value, and returns a mask