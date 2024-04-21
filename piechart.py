import matplotlib.pyplot as plt
import numpy as np

jj = np.array([2,5,8,9,14])
lab = ["Stimul","Anger","Happiness","Stress","Peace"]
myex = [0 , 0 , 0 , 0.2, 0]
col =  [(.8902, 0.8000, 0.8000), (0.6588, 0.4902, 0.3333), (0.6588, 0.6588, 0.3333), (0.6588, 0.6588, 0.6039), (0.8902, 0.7490, 0.6549)]


plt.pie(jj, labels= lab, explode = myex, shadow = True, colors = col)
plt.legend(title = "Mental Statement")
plt.show()
