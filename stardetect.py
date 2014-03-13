import numpy as np

class StarDetect:
    def FindBrightest(image, mask):
        # Finds the brightest unmasked pixel in an image and returns a tuple with its coordinates.
        maskedimg = image * mask
        return np.unravel_index(np.argmax(maskedimg), image.shape)