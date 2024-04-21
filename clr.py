import matplotlib.pyplot as plt
import numpy as np

jj = np.array([2,4,6,8,9,10,12,13,16,17,19])
hh = np.array([1,3,5,6,8,9,10,12,14,16,17])
color = np.array([0,10,20,25,30,35,40,45,50,55,60])

plt.scatter(jj,hh,c = color, cmap ='Accent')

plt.colorbar()
plt.show()