import matplotlib.pyplot as plt
import numpy as np

kk = np.array(["A","B","C","D"])
ll = np.array([2,4,6,8])

plt.bar(kk,ll, width = 0.5)
plt.show()