from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self._size = 0
        self._storage = DoublyLinkedList()

    def push(self, value: int):
        self._storage.add_to_tail(value)
        self._size = len(self._storage)

    def pop(self):
        val = self._storage.remove_from_tail()
        self._size = len(self._storage)
        return val

    def len(self):
        return self._size
