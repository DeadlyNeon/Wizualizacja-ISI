import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n)

fig = plt.figure()
ax = fig.add_subplot(121 , projection = "3d")
n = 20

for c, m, znajn, znajw in [( "m" , "^" , - 50 , - 25 )]:
    ox = randrange(n, 23 , 32 )
    oy = randrange(n, 0 , 100 )
    oz = randrange(n, znajn, znajw)
    ax.scatter(ox, oy, oz, c =c, marker =m, label = "20 pkt")

ax.legend()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax2 = fig.add_subplot(122 , projection = "3d")
z = np.linspace( 0 , 2 * np.pi, 5 )
x = np.sin(z)
y = np.cos(z)
ax2.plot(x, y, z, label = "5 pkt")
ax2.legend()
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")
plt.show()