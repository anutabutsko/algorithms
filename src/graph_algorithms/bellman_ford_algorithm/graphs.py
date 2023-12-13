import numpy as np


# Function to initialize a graph with random edges and weights
def initialize_graph():
    np.random.seed(123)

    EL = []

    N = 10

    for k in range(1, 6):
        EL.append([0, k, np.random.randint(1, N)])

    for k in range(1, 11):
        for j in range(11, 15):
            T1 = np.random.randint(0, 2)
            if T1 == 1:
                EL.append([k, j, np.random.randint(1, N)])

    for k in range(11, 15):
        for j in range(15, 20):
            T2 = np.random.randint(0, 2)
            if T2 == 1:
                EL.append([k, j, np.random.randint(1, N)])

    for k in range(15, 20):
        EL.append([k, 20, np.random.randint(1, N)])

    return EL
