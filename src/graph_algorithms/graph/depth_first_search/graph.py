import random

import numpy as np


def generate_graph(seed=None, n=10, start=1, end=4):
    if seed:
        random.seed(seed)
    N = n
    a = np.random.randint(start, end, (N, N))
    A = (a + a.T)
    for i in range(N):
        A[i, i] = 0
    b = np.random.randint(start, end, size=(N, N))
    B = (b + b.T)
    for i in range(N):
        B[i, i] = 0
    c = np.random.randint(start, end, size=(N, N))
    C = (c + c.T)
    for i in range(N):
        C[i, i] = 0
    Z = np.zeros((N, N), dtype=int)
    R1 = np.block([np.block([A, Z]), Z])
    R2 = np.block([np.block([Z, B]), Z])
    R3 = np.block([np.block([Z, Z]), C])
    P = np.zeros((3 * N, 3 * N), dtype=int)
    for i in range(2):
        for j in range(1, 3):
            P[8 + j - 1, (i + 1) * N + j] = 1
    P = (P + P.T)
    M = np.block([np.block([R1.T, R2.T]), R3.T]) + P

    return M
