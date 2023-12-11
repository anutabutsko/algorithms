from sympy import symbols, diff, Matrix


def f(x, y):
    return (x + 1)**2 + 8 * y**2 - 3 * x - y + 1


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

result = newtons_method(200, 10)  # Minimum was found at x = 0.5 and y = 0.0625 after 1 iterations.

print(result)


'''
Newton's Method
Approach: Newton's method uses both the first and second derivatives (gradient and Hessian) of the function. 
It updates the variables in a way that involves inverting the Hessian matrix at each iteration.
Convergence: It generally converges faster than Gradient Descent, especially close to the minimum, because it 
uses second-order information (curvature).
Use Cases: More effective for small to medium-sized problems due to its faster convergence near the optimum.
'''
