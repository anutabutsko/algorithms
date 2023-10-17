import random
import timeit

from matplotlib import pyplot as plt

"""
Description: This code provides a basic implementation of a hash table. It allows for 
the insertion and retrieval of numeric values. The hash table uses open addressing with 
modular arithmetic and a linear probing to handle collisions.
"""


class HashTable:
    # Initializes the hash table with a given size and sets all slots to None.
    def __init__(self, size):
        self.table = [None for _ in range(size)]

    # Returns a string representation of the hash table.
    def __str__(self):
        return str(self.table)

    # Validates if the provided value is a numeric type (int or float).
    @staticmethod
    def validate(value):
        return type(value) in (int, float)

    # Inserts a numeric value into the hash table.
    def insert(self, value):
        idx = flag = self.hash(value)

        if type(idx) is int:
            # Check if the slot is empty or has the same value.
            if self.table[idx] is None or self.table[idx] == value:
                self.table[idx] = value
                return f'Value {value} added, key = {idx}'

            else:
                # Handle hash collision using linear probing.
                idx += 1

                while idx != flag:
                    # Start from the beginning of the table if reached the end.
                    if idx >= len(self.table):
                        idx = 0
                    # Place the value in the next empty or matching slot.
                    if self.table[idx] is None or self.table[idx] == value:
                        self.table[idx] = value
                        return f'Value {value} added, key = {idx}'

                    idx += 1

            # If the value was not added, return False to indicate that no room is left in the table.
            return False

    # Retrieves a numeric value from the hash table if it exists.
    def search_by_value(self, value):
        idx = flag = self.hash(value)

        if self.table[idx] == value:
            return self.table[idx]

        idx += 1

        while idx != flag:
            if idx >= len(self.table):
                idx = 0

            if self.table[idx] == value:
                return self.table[idx]
            elif self.table[idx] is None:
                return f'Value {value} not fount'

            idx += 1

        return f'Value {value} not fount'

    # Retrieves a numeric value from the hash table by key.
    def search_by_key(self, idx):
        if self.table[idx]:
            return self.table[idx]

        return f'Key {idx} not fount'

    # Computes a hash value using the modulo operation.
    def hash(self, value):
        if self.validate(value):
            return value % len(self.table)

        # Print an error if a non-numeric value is provided.
        print(f'Value "{value}" not added, provide numeric values only')


# Set a random seed for reproducibility.
random.seed(10)

# Generate 1000 distinct random 10-digit numbers.
random_sample = random.sample(range(1000000000, 10000000000 - 1), 1000)

# Generate 50 distinct random numbers between 1 and 1000.
random_keys = random.sample(range(1, 1000), 50)

# Create an instance of the HashTable class.
hashtable = HashTable(size=1021)

# Insert each number from the sample into the hash table.
for num in random_sample:
    result = hashtable.insert(num)
    if result is False:
        print(f'Value {num} not added. Hash table ran out of space, no more values may be inserted.')
        break

    print(result)

# Print the contents of the hash table.
print(hashtable)
print(hashtable.search_by_value(3113295419))

# Initiate an empty list to store runtimes.
runtimes = []

# Test the time required to search the hash table for 50 randomly chosen keys.
for key in random_keys:
    start = timeit.default_timer()
    hashtable.search_by_key(key)
    stop = timeit.default_timer()

    runtimes.append(stop - start)

# Construct a histogram to visualize the results
plt.hist(runtimes)
plt.title("Runtimes of Hash Table")
plt.xlabel("Time in seconds")
plt.ylabel("Number of keys")
plt.grid(True)
plt.show()
