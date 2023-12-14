import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x * np.sin(x)


#set step size:
x0 = 1.57
delta = .2
n = 8
X = [x0]
Y = [f(x0)]

for k in range(0, n):
    if f(X[k] - delta) <= min(f(X[k]), f(X[k] + delta)):
        X.append(X[k] - delta)
        Y.append(f(X[k] - delta))
    else:
        X.append(X[k] + delta)
        Y.append(f(X[k] + delta))

I = [-2]
O = [f(-2)]

for k in range(0, 400):
    I.append(I[k] + .01)
    O.append(f(I[k] + .01))

plt.plot(I, O)
plt.plot(X, Y, "ro")

plt.show()
