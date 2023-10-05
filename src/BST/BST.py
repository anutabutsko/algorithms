class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert(value)

        elif value > self.value:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def traverse(self):
        if self.left:
            self.left.traverse()
        print(self.value)
        if self.right:
            self.right.traverse()

    def search(self, value):
        if value < self.value:
            if not self.left:
                return False
            return self.left.search(value)

        elif value > self.value:
            if not self.right:
                return False
            return self.right.search(value)

        return True


BST = Node(6)
BST.insert(13)
BST.insert(15)
BST.insert(3)
BST.insert(1)
BST.insert(8)
BST.insert(10)
BST.insert(7)
BST.insert(21)
BST.insert(14)

# BST.traverse() # 1 3 6 7 8 10 13 14 15 21

# print(BST.search(14)) # True
# print(BST.search(56)) # False
