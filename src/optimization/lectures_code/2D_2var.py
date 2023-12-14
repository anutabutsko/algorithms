import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def f(x, y):
    return (x + 1) ** 2 + 8 * (y ** 2) - 3 * x - y + 1


x_values = np.arange(-2.0, 0.0, 0.1)
y_values = np.arange(1.0, 3.0, 0.1)
x, y = np.meshgrid(x_values, y_values)
z = f(x, y)

im = plt.imshow(
    z,
    extent=[-2, 0, 1, 3],
    cmap=cm.RdBu,
    origin='lower')

cset = plt.contour(
    z,
    np.arange(-1, 1.5, 0.2),
    linewidths=2,
    cmap=cm.Set2,
    extent=[-2, 0, 1, 3])

plt.clabel(
    cset,
    inline=True,
    fmt='%1.1f',
    fontsize=10)

plt.colorbar(im)

plt.title('z = (x+1)^2 + 8(y^2) - 3x - y + 1')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
