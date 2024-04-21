import matplotlib.pyplot as plt
import numpy as np

jj = np.array([2,4,6,8,9,10,12,13,16,17,19])
hh = np.array([1,3,5,6,8,9,10,12,14,16,17])
size= np.array([0,10,20,250,30,350,40,450,500,55,600])

plt.scatter(jj,hh,s = size, alpha = 0.5)


plt.show()