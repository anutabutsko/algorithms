import timeit
from random import randint
from statistics import mean

import matplotlib.pyplot as plt

"""
Max heapify implementation
Each comparison has constant cost upper bound
Each cost has constant cost upper bound
Because of the recursive nature, the process repeats no more than the height of the heap
The runtime of max_heapify() algorithm is O(log(x))
"""


def max_heapify(array, i):
    n = len(array)
    # Find children
    left = 2 * i + 1
    right = 2 * i + 2

    # Comparing to children
    if left < n and array[left] > array[i]:
        largest = left
    else:
        largest = i

    if right < n and array[right] > array[largest]:
        largest = right

    # Swap with the largest child
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        # Call function recursively until there is a positive comparison, or we reached the bottom of the heap
        max_heapify(array, largest)


"""
Building max heap
The FOR loop executes theta(x) times
Each execution of the FOR loop includes a call to max_heapify()
The other calls in the FOR loop run at constant time
The worst case run time of build_max_heap() is theta(x log(x))
"""


def build_max_heap(array):
    # Find the position of the starting node
    m = len(array) // 2 - 1

    # Iterating through the array starting from the last parent up to the top of the heap
    for i in range(m, -1, -1):
        max_heapify(array, i)

    return array


# Function that generates a random list of given length
def generate_random_list(length):
    return [randint(0, 1000) for _ in range(length)]


# Main script

# Creating a list with lengths that will be used to generate random lists
len_lsts = [i * 20 for i in range(1, 41)]

average_runtimes = []

# Iterating through different array lengths
for len_lst in len_lsts:
    runtimes = []
    # Iterating 1000 times to find the average runtime of build_max_heap() algorithm at a certain length of an array
    for _ in range(1000):
        # Generating random list of size len_lst for every new iteration
        random_list = generate_random_list(len_lst)
        start = timeit.default_timer()
        build_max_heap(random_list)
        stop = timeit.default_timer()

        runtimes.append(stop - start)

    average_runtimes.append(mean(runtimes))

# Creating the plot
plt.plot(len_lsts, average_runtimes)
plt.xlabel('List Size')
plt.ylabel('Average Runtime')
plt.title('Average Runtime of Max Heap Algorithm')
plt.grid(True)

# Saving the plot as a PDF
plt.savefig('Max_Heap.pdf')

# Displaying the plot
plt.show()

"""
We can visualize the average growth of the Max Heap Algorithm in the plot provided in the attached PDF file.
Although we have previously established that T(x) = theta(x log(x)), the plot might give an impression of
linear growth. However, it's essential to underscore that the Max Heap Algorithm's growth rate is indeed
x log(x). As x becomes significantly large, its growth will surpass that of a linear function, showing
a more pronounced curvature in the plot.
"""
