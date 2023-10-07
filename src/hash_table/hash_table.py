import random


class HashTable:
    def __init__(self, size):
        self.table = [None for _ in range(size)]

    def __str__(self):
        return str(self.table)

    @staticmethod
    def validate(value):
        if type(value) in (int, float):
            return True

        return False

    def insert(self, value):
        idx = self.hash(value)
        if idx:
            # check if the slot is empty or has the same value
            if self.table[idx] is None or self.table[idx] == value:
                self.table[idx] = value
            else:
                while True:
                    idx += 1
                    if idx >= len(self.table):
                        idx = 0
                    if self.table[idx] is None or self.table[idx] == value:
                        self.table[idx] = value
                        break

    def get(self, value):
        idx = self.hash(value)
        return self.table[idx]

    def hash(self, value):
        if self.validate(value):
            return value % len(self.table)

        print(f'{value} not added, provide numeric values only')


# set random seed
random.seed(10)

# generate 1000 random numbers length 10
random_sample = random.sample(range(1000000000, 10000000000 - 1), 1000)

hashtable = HashTable(size=1021)

for num in random_sample:
    hashtable.insert(num)


# hashtable.insert('hello')
# hashtable.insert(5)
# hashtable.insert(22)
# print(hashtable.get(2))
print(hashtable)
