import numpy as np
import matplotlib.pyplot as plt


def sigma_sum(start, end, expression):
    return sum(expression(i) for i in range(start, end))


def f(n):
    summation = sigma_sum(1, n, lambda i: 1/i)
    return ((n + 1) ** 2) * summation


def g(n):
    summation = sigma_sum(1, n, lambda i: i + 1/i)
    return np.log(n + 1) * summation


x_values = [i for i in range(100)]

f_values = [f(i) for i in x_values]
g_values = [g(i) for i in x_values]
f_g_values = [f_values[i] / g_values[i] for i in range(len(f_values))]
g_f_values = [g_values[i] / f_values[i] for i in range(len(f_values))]

plt.plot(x_values, g_values, label='g(x)')
plt.plot(x_values, f_values, label='f(x)')
plt.plot(x_values, g_f_values, label='g(x)/f(x)')
plt.plot(x_values, f_g_values, label='f(x)/g(x)')

plt.legend()
plt.show()

"""
As evidenced by the plot 'problem1_plot.png': f(x) = O(g(x)), meaning that f(x) grows faster than g(x) and bounds it
from above.
However, when we plot g(x)/f(x) or f(x)/g(x), they both go to zero.
I ended up using 10 x-values because this is the only way to actually visualize both of the lines on the plot. If we use a 
larger number, for example 50, one line lies on top of another to the point that it isn't possible to see both.
Both of these functions decrease one another and go to zero when plotted this way (g(x)/f(x) and f(x)/g(x)).
"""
