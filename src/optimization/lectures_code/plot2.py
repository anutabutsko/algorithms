import numpy as np
from matplotlib import pyplot as plt, cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


def f(x, y):
    return (x + 1) ** 2 + 8 * (y ** 2) - 3 * x - y + 1


x_values = np.arange(-2.0, 0.0, 0.1)
y_values = np.arange(1.0, 3.0, 0.1)
x, y = np.meshgrid(x_values, y_values)
z = f(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(
    x,
    y,
    z,
    rstride=1,
    cstride=1,
    cmap=cm.RdBu,
    linewidth=0,
    antialiased=False
)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
