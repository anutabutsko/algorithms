"""
Gradient descent algorithms find local minima by moving along the direction of
the steepest descent while Newton's method takes into account curvature information
and thereby often improves convergence.
"""


from sympy import symbols, diff


def f(x):
    return x ** 2 - 2


def df(x):
    return diff(f(x), x)


def newtons_method(x0):
    x = symbols('x')
    counter = 0
    while True:
        f_x0 = f(x).subs(x, x0)
        df_x0 = df(x).subs(x, x0)

        new_x0 = x0 - f_x0 / df_x0

        if round(new_x0, 5) == round(x0, 5):
            break

        x0 = new_x0
        counter += 1

    return f"The root was found to be at {float(x0)} after {counter} iterations."


result = newtons_method(10)

print(result)
