"""
This Python function `search` implements a binary search algorithm capable of searching for an
element in both regular (sorted) lists and pivoted (rotated) lists. The algorithm efficiently finds
the target element in O(log N) time complexity.
"""


def search(lst, elem):
    # Initialize left and right pointers for binary search
    left, right = 0, len(lst) - 1

    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2

        # Check if the element at the middle index is equal to the target element
        if elem == lst[mid]:
            return f"{elem} was found at index {mid}"

        # If the target element is greater than the middle element
        elif elem > lst[mid]:
            # Check if the list is rotated (contains a pivot)
            if lst[left] > lst[right]:
                # Check if the middle element is greater than the rightmost element
                # or if the rightmost element is greater than or equal to the target element
                if lst[mid] > lst[right] or lst[right] >= elem:
                    left = mid + 1  # Adjust the left pointer
                else:
                    right = mid - 1  # Adjust the right pointer
            else:
                left = mid + 1  # Adjust the left pointer

        # If the target element is less than the middle element
        elif elem < lst[mid]:
            # Check if the list is rotated (contains a pivot)
            if lst[left] > lst[right]:
                # Check if the middle element is less than the leftmost element
                # or if the leftmost element is less than or equal to the target element
                if lst[mid] < lst[left] or lst[left] <= elem:
                    right = mid - 1  # Adjust the right pointer
                else:
                    left = mid + 1  # Adjust the left pointer
            else:
                right = mid - 1  # Adjust the right pointer

    return f"{elem} not found"


# Sample list for testing
pivoted_sample = [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]

print(search(pivoted_sample, 0))  # Should print "0 was found at index 6"
