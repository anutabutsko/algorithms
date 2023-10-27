import timeit

import numpy as np


# Peak finder 23
def peak_finder_23(lst):
    # Recording start time
    start = timeit.default_timer()

    rows = len(lst)
    columns = len(lst[0])

    # Splitting the matrix in half by column and find the largest value in that column
    j = columns // 2
    largest = lst[0][j]
    i = 0
    for row in range(1, rows):
        if lst[row][j] > largest:
            largest = lst[row][j]
            i = row

    # Comparing values to left and to the right - continue recursively if one of the values
    # is larger than the selected one - O(nlog x) time
    if j > 0 and lst[i][j] < lst[i][j - 1]:
        return peak_finder_23(lst[:, :j - 1])
    if j < columns - 1 and lst[i][j] < lst[i][j + 1]:
        return peak_finder_23(lst[:, j + 1:])

    # Recording end time
    stop = timeit.default_timer()
    time = stop - start
    return f'{lst[i][j]}, Time: {time:.15f}'


# Creating sample payload
lst_2dim = np.random.choice(1000000, size=(1000, 1000), replace=False)


# Data to visualize THE WORST case running time
lst_2dim2 = np.array([[i for i in range(10000)] for _ in range(1000)])

# Running payload through functions
peak_23 = peak_finder_23(lst_2dim)

# Outputting the result
print(f'Peak finder 23 result: {peak_23}')
