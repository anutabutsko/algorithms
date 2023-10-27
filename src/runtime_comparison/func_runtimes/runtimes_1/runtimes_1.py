import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve


# defining function R1
def r1(n):
    return 4 * (n ** 2) + n


# defining function R2
def r2(n):
    return 64 * n * np.log2(n) + 2 * n


# defining an intersection function between R1 and R2
def intersection(n):
    return r1(n) - r2(n)


# MAIN SCRIPT

n_values = np.linspace(1, 1000000, 1000)  # Generating x values

r1_values = r1(n_values)  # Running x values through R1 function
r2_values = r2(n_values)  # Running x values through R2 function

# Generating the plots
plt.plot(n_values, r1_values, label='R1(x) = 4n^2 + x')
plt.plot(n_values, r2_values, label='R2(x) = 64nlog2(x) + 2n')

# Labels and title
plt.xlabel('x')
plt.ylabel('R(x)')
plt.title('Plot of R1 and R2 functions')
plt.legend()

# Finding the intersection point
intersection_point = fsolve(intersection, x0=100000)
plt.plot(intersection_point, [r1(intersection_point[0])], 'ro', label='Intersection')

# Saving the plot
plt.savefig('R1_R2_functions_plot.pdf')

# Displaying the plot
plt.show()

"""
From the plot, it is evident that the functions R1 and R2 intersect at a single point,
close to x = 0. The R1 function, which is quadratic, exhibits a rapid growth rate even
for small values of x, dominating the growth of R2.
Although it may seem like the R2 function is growing very slowly, creating an illusion
of a constant-time function when plotted alongside R1, it is important to note that it
is not constant; it has a linearithmic growth rate due to the term 64n log₂(x).
Its growth is much slower compared to the quadratic growth of R1, but it still
increases as x gets larger.
To get a clearer understanding of R2’s behavior, we can refer to separate plots for R1
and R2, further down in this file. These plots illustrate grows rates of O(x²) and
O(x log(x)) distinctly.
"""
