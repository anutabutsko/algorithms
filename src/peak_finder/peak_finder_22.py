import timeit

import numpy as np


# Peak finder 22
def peak_finder_22(lst):
    # Recording start time
    start = timeit.default_timer()

    rows = len(lst)
    columns = len(lst[0])

    # Checking every row and every column in matrix until a peak is found - O(x^2) time
    for i in range(rows):
        for j in range(columns):
            if i > 0 and lst[i][j] < lst[i - 1][j]:
                continue
            if j < columns - 1 and lst[i][j] < lst[i][j + 1]:
                continue
            if i < rows - 1 and lst[i][j] < lst[i + 1][j]:
                continue
            if j > 0 and lst[i][j] < lst[i][j - 1]:
                continue

            # Recording end time
            stop = timeit.default_timer()
            time = stop - start
            return f'{lst[i][j]}, Time: {time:.15f}'


# Creating sample payload
lst_2dim = np.random.choice(1000000, size=(1000, 1000), replace=False)

# Data to visualize THE WORST case running time
lst_2dim2 = np.array([[i for i in range(10000)] for _ in range(1000)])

# Running payload through functions
peak_22 = peak_finder_22(lst_2dim2)

# Outputting the result
print(f'Peak finder 22 result: {peak_22}')
