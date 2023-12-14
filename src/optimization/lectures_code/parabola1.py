import matplotlib.pyplot as plt


def f(x):
    return x * x


def df(x):
    return 2 * x


# set step size:
x0 = 1.57
alpha = .2
n = 40

X = [x0]
Y = [f(x0)]

for k in range(0, n):
    X.append(X[k] - alpha * df(X[k]))
    Y.append(f(X[k] - alpha * df(X[k])))

I = [-2]
O = [f(-2)]

for k in range(0, 400):
    I.append(I[k] + .01)
    O.append(f(I[k] + .01))

plt.plot(I, O)
plt.plot(X, Y, "ro")

plt.show()
