import numpy as np
from starprocessor import StarProcessor

s = StarProcessor()

# StarFinder.OpenFile(s)

def FindBrightest(image, mask):
    # Finds the brightest unmasked pixel in an image and returns a tuple with its coordinates.
    maskedimg = image * mask
    return np.unravel_index(np.argmax(maskedimg), image.shape)
    
def MaskStar(image, coords, size=[[12, 12]]):
    pass
    # Masks star based on highest 
    
print FindBrightest(s.img, s.mask)
print np.argmax(s.img)