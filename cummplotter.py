import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

# finds galaxies and stores the corresponding data in the catalogue.

s = StarProcessor()

stars = np.load("catalogue.npy")

print stars

fluxlist = [i['flux'] for i in stars]
values, base = np.histogram(fluxlist, bins=40)
cumulative = np.cumsum(values)
y_error = cumulative**0.5
print cumulative
print y_error
plt.errorbar(base[:-1], cumulative, y_error, c='blue')
#plt.semilogy()
plt.show()