# Max heap implementation
def max_heap(lst, n, i):
    largest = i
    # Calculating positions of left and right children
    left = i * 2 + 1
    right = i * 2 + 2

    # Comparing the largest value to the left child
    if left < n and lst[largest] < lst[left]:
        largest = left

    # Comparing largest value to the right child
    if right < n and lst[largest] < lst[right]:
        largest = right

    # Checking if largest index has been changed
    # No need to swap elements or call function recursively if largest element was not changed
    if largest != i:
        # Swapping the values of the parent with the largest element
        lst[largest], lst[i] = lst[i], lst[largest]

        # Call function recursively to check children values
        max_heap(lst, n, largest)


# MAIN SCRIPT

# Creating sample data
lst = [2, 7, 3, 4, 8, 8, 9, 10, 3, 5, 12]
n = len(lst)
# Starting node position
m = n // 2 - 1

# Building max heap
for i in range(m, -1, -1):
    print(lst)
    print(i)
    max_heap(lst, n, i)

# Displaying max heap
print(f"Max heap is {lst[0]}")
print(lst)
