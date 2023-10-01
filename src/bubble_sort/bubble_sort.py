import timeit
from random import randint
from statistics import mean

import matplotlib.pyplot as plt

"""
The following algorithm takes in an unsorted list and iterates
through every element of the list using a nested loop structure:
the outer loop selects an element and the inner loop compares
this element with every following element in the list.
If the selected element is larger than any of the elements
that follow it, these two elements are passed to the Swap()
function, which swaps their positions, gradually sorting
the list from smallest to largest. This sorting method is known
as "Bubble Sort". Its time complexity is generally represented
as T(n) = O(n²), which can be inferred from the two nested loops
in the algorithm.
"""


# function that generates a random list of given length
def generate_random_list(length) -> list:
    return [randint(0, 1000) for _ in range(length)]


# swap function part of our bubble sort
def swap(input_lst, pos1, pos2) -> list:
    input_lst[pos1], input_lst[pos2] = input_lst[pos2], input_lst[pos1]

    return input_lst


# bubble sort function that iterates through every element and compares them
def bubble_sort(lst) -> list:
    for i in range(0, len(lst)):
        for j in range(len(lst) - 1, i, -1):
            if lst[j] < lst[j - 1]:
                swap(lst, j, j - 1)
    return lst


# MAIN SCRIPT

A = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]  # input list
print(bubble_sort(A))  # output sorted list

# computing the average runtime of the algorithm for 1000 lists
time = []
for _ in range(1000):
    lst = generate_random_list(20)  # generating random list 1000 times
    start = timeit.default_timer()  # start timer
    bubble_sort(lst)  # running each list through our sorting function
    stop = timeit.default_timer()  # stop timer
    time.append(stop - start)  # save the time difference
time = mean(time)  # finding the average of all times recorded

print(f'Average time taken by the bubble sort algorithm to sort 1000 lists, each containing 20 elements is {time:.15f}')

# Code for calculating the average runtimes for 40 lists increasing in size
len_lsts = [i * 20 for i in range(1, 41)]  # creating a list with lengths that will be used to generate random lists
average_runtimes = []
for len_lst in len_lsts:
    runtimes = []  # a list to save runtimes for 1000 iterations of each size list
    for _ in range(1000):  # iterating 1000 times
        random_list = generate_random_list(len_lst)  # generating random list of size len_lst
        start = timeit.default_timer()  # start timer
        bubble_sort(random_list)  # running each list through our sorting function
        stop = timeit.default_timer()  # stop timer

        runtimes.append(stop - start)  # save the time difference

    average_runtimes.append(mean(runtimes))  # saving the average runtime for list size len_lst

# Creating the plot
plt.plot(len_lsts, average_runtimes)
plt.xlabel('List Size')
plt.ylabel('Average Runtime')
plt.title('Average Runtime of Bubble Sort Algorithm')
plt.grid(True)

# Saving the plot as a PDF
plt.savefig('Bubble_sort_runtimes.pdf')

# Displaying the plot
plt.show()

"""
From the generated plot, it is evident that the curve increasingly
assumes a quadratic(n^2) nature as the size of the input n grows.
This illustrates the algorithm's quadratic time complexity, meaning
that the runtime increases quadratically as the number of elements
in the list increases.
"""
