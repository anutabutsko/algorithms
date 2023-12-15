from sympy import symbols, diff


x, y = symbols('x y')

f = (x - 2)**2 + y**2

df_dx = diff(f, x)
df_dy = diff(f, y)

print(df_dx, df_dy)

# Answer: 2*x - 4, 2*y
