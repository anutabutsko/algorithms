from sympy import symbols, diff


x, y = symbols('x y')

f = (x + 1)**2 + 8 * (y ** 2) - 3 * x - y + 1
g = ((x + 1)**2 + y**2) * ((x - 1)**2 + y**2)

df_dx = diff(f, x)
df_dy = diff(f, y)

dg_dx = diff(g, x)
dg_dy = diff(g, y)

print(df_dx, df_dy)
print(dg_dx, dg_dx)
