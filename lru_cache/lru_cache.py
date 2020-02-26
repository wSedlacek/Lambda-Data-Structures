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

        existing_node = self._find_node(key)

        if existing_node:
            self._storage.move_to_front(existing_node)
            return existing_node.value[key]
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

        existing_node = self._find_node(key)
        item = {key: value}

        if existing_node:
            self._storage.delete(existing_node)

        if len(self._storage) >= self._limit:
            self._storage.remove_from_tail()

        self._storage.add_to_head(item)

    def _find_node(self, key: str):
        working_node = self._storage.head
        while working_node:
            if key in working_node.value:
                return working_node

            working_node = working_node.next

        return None
