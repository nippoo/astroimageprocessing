import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

import itertools

# finds galaxies and stores the corresponding data in the catalogue.

s = StarProcessor()

stars = np.load("catalogue.npy")

#print stars

fluxlist = np.array([[i['flux'], i['fluxerror']] for i in stars])
b = 80          #specifies the number of bins for the historgram
values, base = np.histogram(fluxlist[:,0], bins=b)

fluxlist = np.sort(fluxlist,axis=1)

# print np.where(fluxlist[:,0] == 0, fluxlist[:,0], fluxlist[:,1])

x_error = []

for first, second in itertools.izip(base, base[1:]):
     x_error.append(np.std([t[0] for t in fluxlist if ((t[1] > first) & (t[1] < second))]))

#fluxerror = np.array([[np.where(fluxlist[0] > i[0])] for i in base])

#[t for t in fluxlist if (fluxlist[0] > base[0][0])]





cumulative = np.cumsum(values)

#x_error 
y_error = cumulative**0.5

#print cumulative
#print y_error
plt.errorbar(base[:-1], cumulative,y_error,x_error,c='blue')
plt.semilogy()
plt.show()