import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

def los(r, rmin, rmax):

    return (rmax - rmin)*np.random.rand(r)

def losowyk():
    kolory = ('c','b','g','b','r','y')
    return random.choice(kolory)

def losowym():
    znaczniki = ('.', ',', 'p', '<', '>', '1', '2', '3', '4', '8', 'H', '^', '*', 'v', 'h', 'o', '+', 'x', 'D', 'X', 'd', '|', '_')
    return random.choice(znaczniki)

fig = plt.figure()
ax = fig.gca(projection = "3d")
r = 100

kolory = []
znaczniki = []
for x in range(0, 5):
    while(1):
        c = losowyk()
        if(c not in kolory):
            kolory.append(c)
            break

    while(1):
        z = losowym()
        if(z not in znaczniki):
            znaczniki.append(z)
            break

    ox = los(r, random.randint(-10,10), random.randint(-10,10))
    oy = los(r, random.randint(-50,50) , random.randint(-50,50))
    oz = los(r, random.randint(-100, 100), random.randint(-100, 100))
    ax.scatter(ox, oy, oz, c =kolory[x], marker =znaczniki[x])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()