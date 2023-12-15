from sympy import symbols, diff, solve


x, y = symbols('x y')

f = (x - 2)**2 + y**2

f_x = diff(f, x)
f_y = diff(f, y)

critical_points = solve([f_x, f_y])

print(critical_points)

# Answer: {x: 2, y: 0}
