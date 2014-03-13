import numpy as np
from starprocessor import StarProcessor
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

s = StarProcessor()


s.MaskStar([50,50])

plt.clf()
plt.imshow(s.mask)
plt.show()
