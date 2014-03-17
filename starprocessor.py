import numpy as np
import pyfits       # PyFITS at https://pythonhosted.org/pyfits

# Easier to hardcode the file, since we're working with a single file for the moment
filename = 'mosaic.fits'
threshperc = 0.8 # percentage of local maximum star intensity until we consider it no longer a star

class StarProcessor:
    def __init__(self):
		self.OpenFile()
		#self.ConvertFlux()
		self.PreMask()
		#self.RemoveBackground()
	
    def ConvertFlux(self):
	#converts whole image to flux
		self.img = -2.5*np.log10(self.img)
		print self.img
		self.img += self.header['MAGZPT']
		print self.img
	
    def PreMask(self):
	#specfies any intial areas to be masked out and maskes them
	#code to be written
		self.mask[:,0:95] = 0
		self.mask[:,2470:] = 0
		self.mask[0:113,:] = 0
		self.mask[:,0:95] = 0
		self.RecalculateMasked()
	
    def RemoveBackground(self):
	#removes background
		self.img = self.img - np.median(self.img)
		self.img.clip(min=0)
		self.RecalculateMasked()
        
    def OpenFile(self):    
        self.hdudata = pyfits.open(filename) # we hardcode the input data file
        self.img = self.hdudata[0].data # img is a NumPy array with the data
        self.mask = np.ones(self.img.shape, dtype='bool') # create mask with the same dimensions. We set the bit low to mask it
        self.header = pyfits.getheader('mosaic.fits')
        
        self.RecalculateMasked()

    def FindBrightest(self):
        # Finds the brightest unmasked pixel in an image and returns a tuple with its coordinates.
        return np.unravel_index(np.argmax(self.masked), self.img.shape)
    
    def MaskStar(self, coords, radius=100):
        # Masks star based on given pixel value, and returns a mask

        newstar = True
        localmask = np.ones(self.img.shape, dtype='bool')
        threshold = self.img[coords] * threshperc # threshold value (edge of star)
		
		# for y in range(-radius+1,radius):
#             for x in range(-radius+1,+radius):
#                 if ((coords[0]+x)<self.img.shape[0]) and ((coords[1]+y)<self.img.shape[1]):
#                     if((coords[0]+x)>0) and ((coords[1]+y)>0):
#                         if (x**2+y**2)<radius**2:
#                             if self.mask[coords[0]+x,coords[1]+y]:
#                                 self.mask[coords[0]+x,coords[1]+y] = 0
#                             else:
#                                 newstar = False
        print coords                        
        # look directly up first until below threshold
        for x in range(coords[0], coords[0] - radius, -1):
			if x < 0:
				print "break point 1"
				break
			if self.img[x, coords[1]] < threshold: # not a star any more
				break
			else:
				for y in range(coords[1], coords[1] - radius, -1): # left
					if y < 0:
						print "break point 2"
						break
					if self.img[x, y] < threshold: # not a star any more
						break
					else:
						localmask[x, y] = 0
					for y in range(coords[1], coords[1] + radius): # right
						if y >= self.img.shape[1]:
							print "break point 3"
							print "y is ",y," shape 1 is ", self.img.shape[1]
							break
						if self.img[x, y] < threshold: # not a star any more
							break
						else:
							localmask[x, y] = 0
                           
        #now look down 
        for x in range(coords[0], coords[0] + radius):
			if x >= self.img.shape[0]:
				print "break point 4"
				break
			if self.img[x, coords[1]] < threshold: # not a star any more
				break
			else:
				for y in range(coords[1], coords[1] - radius , -1): # left
					if y < 0:
						print "break point 5"
						break
					if self.img[x, y] < threshold: # not a star any more
						break
					else:
						localmask[x, y] = 0
					for y in range(coords[1], coords[1] + radius): # right
						if y >= self.img.shape[1]:
							print "break point 6"
							break
						if self.img[x, y] < threshold: # not a star any more
							break
						else:
							localmask[x, y] = 0
                        
        self.mask = np.logical_and(self.mask, localmask)
							
    	self.RecalculateMasked()
	
    	return newstar
        
    def RecalculateMasked(self):
        self.masked = self.img*self.mask
		