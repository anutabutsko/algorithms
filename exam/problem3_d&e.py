import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return (x - 2)**2 + y**2


def calculate_gradient(x, y):
    return 2*x - 4, 2*y


x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)

X, Y = np.meshgrid(x, y)

Z = f(X, Y)

current_position = (3, 3, f(3, 3))

learning_rate = 0.1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', computed_zorder=False)

ax.plot_surface(X, Y, Z, cmap='viridis')

counter = 0
while True:
    X_derivative, Y_derivative = calculate_gradient(current_position[0], current_position[1])
    X_new, Y_new = current_position[0] - learning_rate * X_derivative, current_position[1] - learning_rate * Y_derivative

    if round(current_position[0], 5) == round(X_new, 5) and round(current_position[1], 5) == round(Y_new, 5):
        break

    current_position = X_new, Y_new, f(X_new, Y_new)

    ax.scatter(*current_position, color='magenta')

    counter += 1


print(f'Local minimum was found at x = {X_new} and y = {Y_new} after {counter} iterations with learning rate {learning_rate}.')
plt.show()

# Answer d: Local minimum was found at x = 2.000009134385233 and y = 2.7403155699954447e-05 after 51 iterations with learning rate 0.1.
# Answer e: Local minimum was found at x = 2.000135113697938 and y = 0.0004053410938176027 after 440 iterations with learning rate 0.01.

