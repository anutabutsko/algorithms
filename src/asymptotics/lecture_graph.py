import matplotlib.pyplot as plt
import numpy as np

# choose sample length
N = 250

# initialize arrays to store values
q1 = np.zeros((N,))
q2 = np.zeros((N,))
q3 = np.zeros((N,))

# fill arrays with function values
for k in range(0, N):
    q1[k] = .5 * (k / 50) ** 2
    q2[k] = 2 * (k / 50) ** 2
    q3[k] = 1 + (k / 50) ** 2 + (k / 50) * np.sin(k / 20)

# plot results
plt.plot(range(0, N), q1, color="blue")
plt.plot(range(0, N), q2, color='blue')
plt.plot(range(0, N), q3, color='green')
plt.axvline(x=120, color='r')
plt.title("Quadratic asymptotics")
plt.xlabel("Input")
plt.ylabel("Output")
plt.show()
