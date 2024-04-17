import matplotlib.pyplot as plt
import numpy as np


xpoints = np.linspace(0, 10, 100)  
ypoints = np.sin(xpoints) + 0.5 * np.random.randn(100)


plt.figure(figsize=(8, 6))  
plt.plot(xpoints, ypoints, label='Angel Bae', color='k', linestyle='--', marker='o')

plt.title('Customized Sinusoidal Plot: Angel Bae')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()


plt.show()
