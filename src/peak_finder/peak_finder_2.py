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


# Creating sample payload
lst_1dim = sample(range(0, 1000000), 1000000)

# Data to visualize THE WORST case running time
lst_1dim2 = [i for i in range(10000)]

# Running payload through functions
peak_2 = peak_finder_2(lst_1dim)

# Outputting the result
print(f'Peak finder 2 result: {peak_2}')
