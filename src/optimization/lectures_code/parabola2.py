import matplotlib.pyplot as plt


def f(x):
    return x * x


def df(x, y):
    return (f(x + y) - f(x)) / y


# set step size:
x0 = 1.57
delta = .1
alpha = .2
n = 80

X = [x0]
Y = [f(x0)]
for k in range(0, n):
    if f(X[k] - delta) <= min(f(X[k]), f(X[k] + delta)):
        X.append(X[k] - alpha * df(X[k], -delta))
        Y.append(f(X[k] - alpha * df(X[k], -delta)))
    else:
        X.append(X[k] + alpha * df(X[k], delta))
        Y.append(f(X[k] + alpha * df(X[k], delta)))

I = [-2]
O = [f(-2)]

for k in range(0, 400):
    I.append(I[k] + .01)
    O.append(f(I[k] + .01))

plt.plot(I, O)
plt.plot(X, Y, "ro")

plt.show()
