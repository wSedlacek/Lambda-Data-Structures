from typing import List, Optional


class BinarySearchTree:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["BinarySearchTree"] = None
        self.right: Optional["BinarySearchTree"] = None

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return self.value

    def insert(self, value: int):
        """Insert the given value into the tree"""

        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def contains(self, target: int):
        """Return True if the tree contains the value
        False if it does not"""
        if self.value == target:
            return True
        elif self.value < target and self.right:
            return self.right.contains(target)
        elif self.value >= target and self.left:
            return self.left.contains(target)
        else:
            return False

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        """Call the function `cb` on the value of each node
        You may use a recursive or iterative approach"""
        cb(self.value)
        if self.right:
            self.right.for_each(cb)

        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    def in_order_print(self, node):
        """Print all the values in order from low to high
        Hint:  Use a recursive, depth first traversal"""
        if node.left:
            node.in_order_print(node.left)

        print(node.value)

        if node.right:
            node.in_order_print(node.right)

    def bft_print(self, node, root_node=True):
        """Print the value of every node, starting with the given node,
        in an iterative breadth first traversal"""

        if root_node:
            print(node.value)

        if node.left:
            print(node.left)

        if node.right:
            print(node.right)

        if node.left:
            node.bft_print(node.left, False)

        if node.right:
            node.bft_print(node.right, False)

    def dft_print(self, node):
        """Print the value of every node, starting with the given node,
        in an iterative depth first traversal"""
        print(node.value)

        if node.left:
            node.dft_print(node.left)

        if node.right:
            node.dft_print(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    def pre_order_dft(self, node):
        """Print Pre-order recursive DFT"""
        pass

    def post_order_dft(self, node):
        """Print Post-order recursive DFT"""
        pass
