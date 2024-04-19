import numpy as np
import matplotlib.pyplot as plt

x = np.array([2,9,11,20])
y = np.array([9,11,22,31])

fontl = {'family':'serif','color':'black','size':20}
fontll = {'family':'serif','color':'darkred','size':11}

plt.title("Roger's Plot", fontdict = fontl, loc = 'left')
plt.xlabel("How long we haven't met", fontdict = fontll)
plt.ylabel("How long we won't meet", fontdict = fontll)

plt.plot(x,y)
plt.grid()
plt.show()