import matplotlib.pyplot as plt


def f(x):
    return x ** 2


x_values = [i for i in range(100)]
y_values = [f(i) for i in range(100)]


plt.plot(x_values, y_values)

plt.show()
