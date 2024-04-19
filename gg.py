import numpy as np
import matplotlib.pyplot as plt

kk =np.linspace(0,10,80)
ll = np.sin(kk) + 0.5*np.random.randn(80)

plt.figure(figsize=(8, 6))
plt.plot(kk, ll, label='Angel Bae', color='k', linestyle='--', marker='D')

plt.title('Customized Sinusoidal Plot: Angel Bae')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()


plt.show()