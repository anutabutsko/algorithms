"""
The definition of a critical point is one where the derivative is either 0 or undefined.
In order to find the critical points of a function, simply take the derivative of the
function, set it equal to zero, and then solve for x. Moreover, find any values in
the domain where the derivative does not exist because these will also be critical
points.
"""


from sympy import symbols, diff, solve


x, y = symbols('x y')

f = (x + 1) ** 2 + 8 * (y ** 2) - 3 * x - y + 1

f_x = diff(f, x)
f_y = diff(f, y)

# solve the equation
critical_points = solve([f_x, f_y])

print(critical_points)
