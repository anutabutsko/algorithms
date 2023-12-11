import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x, y = sp.symbols('x y')


def g(x, y):
    return ((x + 1) ** 2 + y ** 2) * ((x - 1) ** 2 + y ** 2)


def dg(x, y):
    return (2 * x - 2) * (y ** 2 + (x + 1) ** 2) + (2 * x + 2) * (y ** 2 + (x - 1) ** 2), (2 * x - 2) * (
                y ** 2 + (x + 1) ** 2) + (2 * x + 2) * (y ** 2 + (x - 1) ** 2)


x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)

X, Y = np.meshgrid(x, y)

G = g(X, Y)

current_position = (3, 4.5, g(3, 4.5))

learning_rate = 0.001

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d', computed_zorder=False)

ax.plot_surface(X, Y, G, cmap='viridis')

ax.scatter(*current_position, color='magenta')

counter = 0
while True:
    X_derivative, Y_derivative = dg(current_position[0], current_position[1])
    X_new, Y_new = current_position[0] - learning_rate * X_derivative, current_position[
        1] - learning_rate * Y_derivative

    if round(current_position[0], 5) == round(X_new, 5) and round(current_position[1], 5) == round(Y_new, 5):
        break

    current_position = X_new, Y_new, g(X_new, Y_new)

    ax.scatter(*current_position, color='magenta')

    counter += 1

print(f'Local minimum was found at x = {X_new} and y = {Y_new} after {counter} iterations with learning rate {learning_rate}.')
plt.show()

# Local minimum was found at x = -0.00015633556227153818 and y = 1.499843664437728 after 182 iterations with learning rate 0.01.
# Local minimum was found at x = 0.0019250338404510057 and y = 1.5019250338404488 after 1000 iterations with learning rate 0.001.

'''
Reaching the minima of function g() was significantly faster compared to function f(). 
This difference can be attributed to several factors:
1. Function Shape: The functions f() and g() have completely different shapes, influencing how quickly the 
minima can be reached.
2. Starting Point: Despite having the same starting points for both functions, their paths to the minima were 
different.
3. Gradient Steepness: Comparisons at learning rates of 0.01 and 0.001 showed that g() consistently reached 
its minima much quicker than f(). This suggests that the gradient steepness, affecting the speed, differs 
substantially between the two functions.
The majority of computational work for function g() occurred as the point got closer to the minima. 
This is evident from the 'g_function_0.01.png' plot, which shows a rapid initial decrease towards the minima, 
followed by a slower phase as the point approaches the minima.
'''