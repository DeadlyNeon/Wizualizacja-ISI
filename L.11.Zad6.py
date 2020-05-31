import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def randrange(r, rmin, rmax):
    return (rmax - rmin)*np.random.rand(r)

fig = plt.figure()
ax = fig.add_subplot(121 , projection = "3d")
r = 20

for c, m, znajn, znajw in [( "m" , "^" , - 50 , - 25 )]:
    ox = randrange(r, 23 , 32 )
    oy = randrange(r, 0 , 100 )
    oz = randrange(r, znajn, znajw)
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