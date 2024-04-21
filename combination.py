import matplotlib.pyplot as plt
import numpy as np


jj = np.random.randint(100, size=(100))
hh = np.random.randint(100, size =(100))
size= 10 * np.random.randint(100, size = (100))
color = np.random.randint(100, size=(100))

plt.title("Angel's Party")
plt.scatter(jj,hh,s = size, alpha = 0.5, c = color, cmap ='plasma' )

plt.colorbar()
plt.show()