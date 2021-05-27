from doubly_linked_list import DoublyLinkedList


class LRUCache:
    def __init__(self, limit: int = 10):
        """
        Our LRUCache class keeps track of the max number of nodes it
        can hold, the current number of nodes it is holding, a doubly-
        linked list that holds the key-value entries in the correct
        order, as well as a storage dict that provides fast access
        to every node stored in the cache.
        """
        self._cache = {}
        self._storage = DoublyLinkedList()
        self._limit = limit

    def get(self, key: str):
        """
        Retrieves the value associated with the given key. Also
        needs to move the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """

        if key in self._cache:
            self._storage.move_to_front(self._cache[key])
            return self._cache[key].value[1]
        else:
            return None

    def set(self, key: str, value):
        """
        Adds the given key-value pair to the cache. The newly-
        added pair should be considered the most-recently used
        entry in the cache. If the cache is already at max capacity
        before this entry is added, then the oldest entry in the
        cache needs to be removed to make room. Additionally, in the
        case that the key already exists in the cache, we simply
        want to overwrite the old value associated with the key with
        the newly-specified value.
        """

        if key in self._cache:
            self._storage.delete(self._cache[key])
            del self._cache[key]

        if len(self._storage) >= self._limit:
            last = self._storage.tail
            del self._cache[last.value[0]]
            self._storage.delete(last)

        self._storage.add_to_head((key, value))
        self._cache[key] = self._storage.head
