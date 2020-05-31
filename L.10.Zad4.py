import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(0, 30, 0.1)
n = np.sin(x)
y1 = np.sin(-x)
y = n+2


plt.plot (x,y, label='sin(x)')
plt.plot (x,y1, label='sin(x)')
plt.xlabel ('os x')
plt.ylabel ('os y')
plt.legend()
plt.show()