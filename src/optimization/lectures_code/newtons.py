import math

# initialize
k = 1
X = [5]
Y = [5]
X.append(X[0] - (X[0] + 1))
Y.append(Y[0] - (Y[0] + 1))

# Update until stable to 5 digits or 10000 iterations.
while (((math.floor((X[len(X) - 2] * 10 ** 5 - X[len(X) - 1] * 10 ** 5)) != 0) or
        (math.floor((Y[len(Y) - 2] * 10 ** 5 - Y[len(Y) - 1] * 10 ** 5)) != 0)) and k <= 10000):
    X.append(X[len(X) - 1] - (X[len(X) - 1] + 1))
    Y.append(Y[len(Y) - 1] - (Y[len(Y) - 1] + 1))
    k = k + 1

print(X[len(X) - 1], Y[len(Y) - 1], k)
