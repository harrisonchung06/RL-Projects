import numpy as np
#import matplotlib.pyplot as plt
import utils

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.plot(i,y)
    plt.pause(0.05)

plt.show()