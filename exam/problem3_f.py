from random import randint, seed
from statistics import mean

import numpy as np


seed(123)


def f(x, y):
    return (x - 2)**2 + y**2


def calculate_gradient(x, y):
    return 2*x - 4, 2*y


x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)

X, Y = np.meshgrid(x, y)

Z = f(X, Y)

learning_rate = 0.1

iterations = []
for _ in range(100):
    x_start = randint(-3, 3)
    y_start = randint(-3, 3)

    current_position = (x_start, y_start, f(x_start, y_start))

    counter = 0
    while True:
        X_derivative, Y_derivative = calculate_gradient(current_position[0], current_position[1])
        X_new, Y_new = current_position[0] - learning_rate * X_derivative, current_position[1] - learning_rate * Y_derivative

        if round(current_position[0], 5) == round(X_new, 5) and round(current_position[1], 5) == round(Y_new, 5):
            break

        current_position = X_new, Y_new, f(X_new, Y_new)

        counter += 1

    iterations.append(counter)


print(mean(iterations))

# Answer: 49.14
