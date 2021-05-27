from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self._storage = DoublyLinkedList()
        self._size = 0

    def enqueue(self, value: int):
        self._storage.add_to_tail(value)
        self._size = len(self._storage)

    def dequeue(self):
        val = self._storage.remove_from_head()
        self._size = len(self._storage)
        return val

    def len(self):
        return self._size
