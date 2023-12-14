import matplotlib.pyplot as plt
import math


def f(n):
    return math.log(4 * (n ** 2) + n + 10, 2)


def g(n):
    return 2 * n + 7


x_values = [i for i in range(50)]

f_values = [f(i) for i in x_values]
g_values = [g(i) for i in x_values]
f_g_values = [f_values[i] / g_values[i] for i in range(50)]
g_f_values = [g_values[i] / f_values[i] for i in range(50)]

plt.plot(x_values, g_values, label='g(x)')
plt.plot(x_values, f_values, label='f(x)')
plt.plot(x_values, g_f_values, label='g(x)/f(x)')
plt.plot(x_values, f_g_values, label='f(x)/g(x)')

plt.legend()
plt.show()
