import numpy as np
import matplotlib.pyplot as plt


# multidimensional function z
def z_function(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5


def calculate_gradient(x, y):
    return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * x) * np.sin(5 * y)


def compute_position(position):
    X_derivative, Y_derivative = calculate_gradient(position[0], position[1])
    X_new, Y_new = position[0] - learning_rate * X_derivative, position[1] - learning_rate * Y_derivative

    new_position = X_new, Y_new, z_function(X_new, Y_new)

    return new_position


x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)

Z = z_function(X, Y)

current_position_1 = (0.7, 0.4, z_function(0.7, 0.4))
current_position_2 = (0.8, 0.3, z_function(0.8, 0.3))
current_position_3 = (0.3, 0.9, z_function(0.3, 0.9))
current_position_4 = (-0.5, 0.6, z_function(-0.5, 0.6))

learning_rate = 0.01

ax = plt.subplot(projection='3d', computed_zorder=False)


for _ in range(1000):
    current_position_1 = compute_position(current_position_1)
    current_position_2 = compute_position(current_position_2)
    current_position_3 = compute_position(current_position_3)
    current_position_4 = compute_position(current_position_4)

    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.scatter(current_position_1[0], current_position_1[1], current_position_1[2], color='magenta', zorder=1)
    ax.scatter(current_position_2[0], current_position_2[1], current_position_2[2], color='green', zorder=1)
    ax.scatter(current_position_3[0], current_position_3[1], current_position_3[2], color='cyan', zorder=1)
    ax.scatter(current_position_4[0], current_position_4[1], current_position_4[2], color='orange', zorder=1)

    plt.pause(0.001)
    ax.clear()