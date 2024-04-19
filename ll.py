import matplotlib.pyplot as plt
import numpy as np

kk = np.array([0,1,2,3,])
ll = np.array([3,8,1,10])

plt.subplot(2,1,1)
plt.plot(kk,ll)

kk = np.array([0,1,2,3])
ll = np.array([10,20,30,40])

plt.subplot(2,1,2)
plt.plot(kk,ll)

plt.show()