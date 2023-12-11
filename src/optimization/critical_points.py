from sympy import symbols, diff, solve


x, y = symbols('x y')

f = (x + 1) ** 2 + 8 * (y ** 2) - 3 * x - y + 1

f_x = diff(f, x)
f_y = diff(f, y)

# solve the equation
critical_points = solve([f_x, f_y])

print(critical_points)
