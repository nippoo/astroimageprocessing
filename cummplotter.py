import numpy as np
from starprocessor import StarProcessor

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

import itertools

import csv

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
     x_error.append(np.std([t[0] for t in fluxlist if ((t[1] >= first) & (t[1] < second))]))

#fluxerror = np.array([[np.where(fluxlist[0] > i[0])] for i in base])

#[t for t in fluxlist if (fluxlist[0] > base[0][0])]

print x_error



cumulative = np.cumsum(values)

#x_error 
y_error = cumulative**0.5
cumulative_log=np.log10(cumulative)
y_error_log=y_error*(2*cumulative*np.log(10))**-1

with open('cumplot_data_inc_errors.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['base','x_error','cumulative','y_error','log10(N)','y_error_log'])
    for i in range(len(base)-1):
        spamwriter.writerow([base[i],x_error[i], cumulative[i], y_error[i], cumulative_log[i], y_error_log[i]])
        


#print cumulative
#print y_error
plt.errorbar(base[:-1], cumulative,y_error,x_error,c='blue')
plt.semilogy()
plt.show()


