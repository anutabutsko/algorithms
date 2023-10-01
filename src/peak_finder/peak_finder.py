import timeit
from random import sample

import numpy as np

"""
TODO Add description
"""


# Checking if the list is empty or if there is only one element in the list
def validate(lst):
    if not lst:
        return 'List is empty.'
    n = len(lst)
    p = lst[0]
    if n == 1:
        return p
    return False


# Peak finder 2
def peak_finder_2(lst) -> str:
    # Recording start time
    start = timeit.default_timer()

    # Checking if the list is empty or if there is only one element in the list
    if validate(lst):
        stop = timeit.default_timer()
        time = stop - start
        return f'{validate(lst)}, Time: {time:.15f}'

    n = len(lst)
    p = lst[0]
    j = 1
    # Iterating through every element in the list and comparing to the following value - O(n) time
    while j < n and p < lst[j]:
        p = lst[j]
        j += 1

    # Recording end time
    stop = timeit.default_timer()
    time = stop - start
    return f'{p}, Time: {time:.15f}'


# Peak finder 3
def peak_finder_3(lst):
    # Recording start time
    start = timeit.default_timer()

    # Checking if the list is empty or if there is only one element in the list
    if validate(lst):
        stop = timeit.default_timer()
        time = stop - start
        return f'{validate(lst)}, Time: {time:.15f}'

    # Splitting the list in half and comparing values on both sides.
    # Continue recursively if one of the values is larger than the selected one - O(log n) time
    n = len(lst)
    m = n // 2
    if lst[m] < lst[m - 1]:
        return peak_finder_3(lst[:m])
    elif lst[m] > lst[m - 1]:
        return peak_finder_3(lst[m:])

    # Recording end time
    stop = timeit.default_timer()
    time = stop - start
    return f'{lst[m]}, Time: {time:.15f}'


# Peak finder 22
def peak_finder_22(lst):
    # Recording start time
    start = timeit.default_timer()

    # Checking if the array is one dimensional
    if isinstance(lst, list):
        return peak_finder_3(lst)  # If true - run through peak finder 3 and return result

    rows = len(lst)
    columns = len(lst[0])

    # Checking every row and every column in matrix until a peak is found - O(n^2) time
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


# Peak finder 23
def peak_finder_23(lst):
    # Recording start time
    start = timeit.default_timer()

    # Checking if the array is one dimensional
    if isinstance(lst, list):
        return peak_finder_3(lst)  # If true - run through peak finder 3 and return result

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
    # is larger than the selected one - O(nlog n) time
    if j > 0 and lst[i][j] < lst[i][j - 1]:
        return peak_finder_23(lst[:, :j - 1])
    if j < columns - 1 and lst[i][j] < lst[i][j + 1]:
        return peak_finder_23(lst[:, j + 1:])

    # Recording end time
    stop = timeit.default_timer()
    time = stop - start
    return f'{lst[i][j]}, Time: {time:.15f}'


# Creating sample data
lst_1dim = sample(range(0, 1000000), 1000000)
lst_2dim = np.random.choice(1000000, size=(1000, 1000), replace=False)
print(lst_1dim)

# Data to visualize THE WORST case running time
lst_1dim2 = [i for i in range(10000)]
lst_2dim2 = np.array([[i for i in range(10000)] for _ in range(1000)])

# Running data through functions
peak_2 = peak_finder_2(lst_1dim)
peak_3 = peak_finder_3(lst_1dim)
peak_22 = peak_finder_22(lst_2dim2)
peak_23 = peak_finder_23(lst_2dim)

# peak_2 = peak_finder_2(lst_1dim2)
# peak_3 = peak_finder_3(lst_1dim2)
# peak_22 = peak_finder_22(lst_2dim2)
# peak_23 = peak_finder_23(lst_2dim2)


# Outputting the result
print(f'Peak finder 2 result: {peak_2}')
print(f'Peak finder 3 result: {peak_3}')
print(f'Peak finder 22 result: {peak_22}')
print(f'Peak finder 23 result: {peak_23}')
