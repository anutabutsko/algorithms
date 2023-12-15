from sympy import symbols, diff, Matrix


def f(x, y):
    return (x**2 + y**2) * ((x - 2)**2 + y**2)


# first derivative
def gradient():
    return Matrix([diff(f(x, y), x), diff(f(x, y), y)])


# second derivative
def hessian():
    g = gradient()
    return Matrix([[diff(g[0], x), diff(g[0], y)],
                   [diff(g[1], x), diff(g[1], y)]])


def newtons_method(x0, y0):
    counter = 0

    while True:
        grad = gradient().subs({x: x0, y: y0})
        H = hessian().subs({x: x0, y: y0})

        new_x, new_y = Matrix([x0, y0]) - H.inv() * grad

        if round(new_x, 5) == round(x0, 5) and round(new_y, 5) == round(y0, 5):
            return f'Minimum was found at x = {float(new_x)} and y = {float(new_y)} after {counter} iterations.'

        counter += 1

        x0, y0 = new_x, new_y


x, y = symbols('x y')

result = newtons_method(0.2, 0.2)

print(result)

# Answer: Minimum was found at x = -3.6280936367709984e-12 and y = -2.767070779534139e-13 after 4 iterations.
