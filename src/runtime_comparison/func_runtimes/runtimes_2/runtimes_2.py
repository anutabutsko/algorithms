import numpy as np
import matplotlib.pyplot as plt


def f1(n):
    return n ** 2


def f2(n):
    return np.full_like(n, 2)


def f3(n):
    return 2 ** n


def f4(n):
    return np.log2(n)


def f5(n):
    return (1 / 2) * n


def f6(n):
    return n * np.log2(n)


def f7(n):
    return n


def f8(n):
    return n ** 3


def f_plot(n_values, f_values):
    plt.plot(n_values, f_values)


n_values = np.linspace(1, 4, 100)

f1_values = f1(n_values)
f2_values = f2(n_values)
f3_values = f3(n_values)
f4_values = f4(n_values)
f5_values = f5(n_values)
f6_values = f6(n_values)
f7_values = f7(n_values)
f8_values = f8(n_values)

plt.plot(n_values, f1_values, label='f1(n)=n^2')
plt.plot(n_values, f2_values, label='f2(n)=2')
plt.plot(n_values, f3_values, label='f3(n)=2^n')
plt.plot(n_values, f4_values, label='f4(n)=log2(n)')
plt.plot(n_values, f5_values, label='f5(n)=(1/2)n')
plt.plot(n_values, f6_values, label='f6(n)=n log2(n)')
plt.plot(n_values, f7_values, label='f7(n)=n')
plt.plot(n_values, f8_values, label='f8(n)=n^3')

plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('Function Growth Comparison')
plt.legend()
plt.grid(True)

plt.show()
