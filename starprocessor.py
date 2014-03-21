import numpy as np
import pyfits       # PyFITS at https://pythonhosted.org/pyfits

# Easier to hardcode the file, since we're working with a single file for the moment
filename = 'mosaic.fits'
maskthreshold = 35000

class StarProcessor:
    def __init__(self):
        self.OpenFile()
        #self.MaskAboveThreshold()
		#self.ConvertFlux()	#work with counts to start with not flux
		#self.PreMask()
		#self.RemoveBackground()
	
    def ConvertFlux(self):
	#converts whole image to flux
		self.img = -2.5*np.log10(self.img)
		self.img += self.header['MAGZPT']
		self.RecalculateMasked()
		
    def flux(self, coords):
    #returns flux at given coordinates, converting the count reading into flux using the predefined MAGZPT value.
	return self.header['MAGZPT'] - 2.5*np.log10(self.img[coords])

	
    def PreMask(self):
	#specfies any intial areas to be masked out and maskes them
	#code to be written
		self.RecalculateMasked()
	
    def RemoveBackground(self):
	#removes background
		self.img = self.img - np.median(self.img)
		self.img.clip(min=0)
		self.RecalculateMasked()
        
    def OpenFile(self):    
        self.hdudata = pyfits.open(filename) # we hardcode the input data file
        self.img = self.hdudata[0].data # img is a NumPy array with the data
        self.img = self.img[113:4512, 95:2470] #cuts off the noisy edges
        self.mask = np.ones(self.img.shape, dtype='bool') # create mask with the same dimensions. We set the bit low to mask it
        self.header = pyfits.getheader('mosaic.fits')
        
        self.RecalculateMasked()

    def FindBrightest(self):
        # Finds the brightest unmasked pixel in an image and returns a tuple with its coordinates.
        return np.unravel_index(np.argmax(self.masked), self.img.shape)
        
    def MaskAboveThreshold(self):
        self.mask[self.img > maskthreshold] = False
        self.RecalculateMasked()
    
    def MaskStar(self, coords, radius=700, threshperc = 0.10): 			# percentage of local maximum star intensity until we consider it no longer a star
        # Masks star based on given pixel value, and returns a mask
        newstar = True
        localmask = np.ones(self.img.shape, dtype='bool')
        #threshold = self.img[coords] + threshval # threshold value (edge of star)
        threshold = self.img[coords]*threshperc
        print threshold

        print coords                        
        # look directly up first until below threshold
        for x in range(coords[0], coords[0] - radius, -1):
			print "up: x=", x
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
					if self.img[x, y]==0:
						newstar = false
						print "not new star"
					if self.img[x, y] < threshold: # not a star any more
						break
					else:
						localmask[x, y] = 0
					for y in range(coords[1], coords[1] + radius): # right
						if y >= self.img.shape[1]:
							print "break point 3"
							break
						if self.img[x, y] == 0:
							newstar = false
							print "not new star"
						if self.img[x, y] < threshold: # not a star any more
							break
						else:
							localmask[x, y] = 0
                           
        #now look down 
        for x in range(coords[0], coords[0] + radius):
			print "down: x=", x
			if x >= self.img.shape[0]:
				#print "break point 4"
				break
			if self.img[x, coords[1]] < threshold: # not a star any more
				break
			else:
				for y in range(coords[1], coords[1] - radius , -1): # left
					if y < 0:
						print "break point 5"
						break
					if self.img[x, y] == 0:
						newstar = false
						print "not new star"
					if self.img[x, y] < threshold: # not a star any more
						break
					else:
						localmask[x, y] = 0
					for y in range(coords[1], coords[1] + radius): # right
						if y >= self.img.shape[1]:
							print "break point 6"
							break
						if self.img[x, y] == 0:
							newstar = false
							print "not new star"
						if self.img[x, y] < threshold: # not a star any more
							break
						else:
							localmask[x, y] = 0
                        
        self.mask = np.logical_and(self.mask, localmask)
							
    	self.RecalculateMasked()
	
    	return newstar
	
    def MaskGalaxy(self, coords, Gradius = 6, Bradius=12):
        localmask = np.ones(self.img.shape, dtype='bool')
        Tcount = 0
        Tbckgnd = 0
        Agal = 0
        Abckgnd = 0
        #algorithm to caluclate average count of a galaxy
        for y in range(-Bradius+1,Bradius):
        	for x in range(-Bradius+1,+Bradius):
        		if ((coords[0]+x)<self.img.shape[0]) and ((coords[1]+y)<self.img.shape[1]):
        			if((coords[0]+x)>0) and ((coords[1]+y)>0):
        				if (x**2+y**2)<Bradius**2 and (x**2+y**2)>Gradius:
        					Tbckgnd = Tbckgnd + self.img[coords]
        					Abckgnd = Abckgnd + 1
        					print "background pixel"
        				if (x**2+y**2)<Gradius:
        					Tcount = Tcount + self.img[coords] 
        					Agal = Agal + 1
        					print "galaxy pixel"
        plt.clf()
        plt.imshow(localmask)
        plt.show()					
        localbck = Tbckgnd/Abckgnd
        print "localbck", localbck
        avecount = Tcount/Agal
        print "average count", avecount
        avecount = avecount-localbck
        print "true <count>", avecount
        self.mask = np.logical_and(self.mask, localmask)					
        self.RecalculateMasked()
        return avecount
    
    def RecalculateMasked(self):
        self.masked = self.img*self.mask
        
    def MaskCircle(self, coords, radius=12):
            for y in range(-radius+1,radius):
                for x in range(-radius+1,+radius):
                    if ((coords[0]+x)<self.img.shape[0]) and ((coords[1]+y)<self.img.shape[1]):
                        if((coords[0]+x)>0) and ((coords[1]+y)>0):
                            if (x**2+y**2)<radius**2:
                                if self.mask[coords[0]+x,coords[1]+y]:
                                    self.mask[coords[0]+x,coords[1]+y] = 0
                                else:
                                    newstar = False
            self.RecalculateMasked()                
            return newstar
		