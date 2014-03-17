import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path



s = StarProcessor()




plt.clf()
plt.imshow(s.img)
plt.show()
