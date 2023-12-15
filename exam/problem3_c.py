from sympy import symbols, diff, Matrix


def f(x, y):
    return (x - 2)**2 + y**2


# first derivative
def gradient():
    return Matrix([diff(f(x, y), x), diff(f(x, y), y)])


# second derivative
def hessian():
    g = gradient()
    return Matrix([[diff(g[0], x), diff(g[0], y)],
                   [diff(g[1], x), diff(g[1], y)]])


x, y = symbols('x y')

H = hessian().subs({x: x, y: y})

print(hessian())

# Answer: Matrix([[2, 0],
#                [0, 2]])
