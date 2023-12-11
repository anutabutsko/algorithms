import numpy as np
import matplotlib.pyplot as plt


def z_function(x, y):
    return (x + 1) ** 2 + 80 * (y ** 2) - 3 * x - y + 1


def calculate_gradient(x, y):
    return 2 * x - 1, 16 * y - 1


x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)

X, Y = np.meshgrid(x, y)

Z = z_function(X, Y)

current_position = (3, 4.5, z_function(3, 4.5))

learning_rate = 0.001

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', computed_zorder=False)

ax.plot_surface(X, Y, Z, cmap='viridis')

counter = 0
while True:
    X_derivative, Y_derivative = calculate_gradient(current_position[0], current_position[1])
    X_new, Y_new = current_position[0] - learning_rate * X_derivative, current_position[1] - learning_rate * Y_derivative

    if round(current_position[0], 5) == round(X_new, 5) and round(current_position[1], 5) == round(Y_new, 5):
        break

    current_position = X_new, Y_new, z_function(X_new, Y_new)

    ax.scatter(*current_position, color='magenta')

    counter += 1


print(f'Local minimum was found at x = {X_new} and y = {Y_new} after {counter} iterations with learning rate {learning_rate}.')
plt.show()

# Local minimum was found at x = 0.5004051396119912 and y = 0.06250000000000004 after 431 iterations with learning rate 0.01.
# Local minimum was found at x = 0.5048152678422779 and y = 0.06250000000000043 after 3122 iterations with learning rate 0.001.

# changing coefficient 8 to 80 did not change the number of iterations to reach the minimum
