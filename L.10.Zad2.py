import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [x for x in range(1,21)]
y = [1/x for x in range(1,21)]
plt.plot(x, y, linestyle='dotted',marker='>', color='green' ,label='x^-1')
plt.axis([1,20,0,1])
plt.ylabel('f(x)')
plt.xlabel('x')
plt.legend()
plt.show()