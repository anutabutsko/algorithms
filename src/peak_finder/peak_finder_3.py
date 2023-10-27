import timeit
from random import sample


# Checking if the list is empty or if there is only one element in the list
def validate(lst):
    if not lst:
        return 'List is empty.'
    n = len(lst)
    p = lst[0]
    if n == 1:
        return p
    return False


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
    # Continue recursively if one of the values is larger than the selected one - O(log x) time
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


# Creating sample payload
lst_1dim = sample(range(0, 1000000), 1000000)

# Data to visualize THE WORST case running time
lst_1dim2 = [i for i in range(10000)]

# Running payload through functions
peak_3 = peak_finder_3(lst_1dim)

# Outputting the result
print(f'Peak finder 3 result: {peak_3}')
