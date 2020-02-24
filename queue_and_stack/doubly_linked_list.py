from typing import Optional


class ListNode:
    """Each ListNode holds a reference to its previous node
    as well as its next node in the List."""

    def __init__(self, value: int, prev: Optional["ListNode"] = None, next: Optional["ListNode"] = None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value: int):
        """Wrap the given value in a ListNode and insert it
        after this node. Note that this node could already
        have a next node it is point to."""

        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value: int):
        """Wrap the given value in a ListNode and insert it
        before this node. Note that this node could already
        have a previous node it is point to."""

        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        """Rearranges this ListNode's previous and next pointers
        accordingly, effectively deleting this ListNode."""

        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    """Our doubly-linked list class. It holds references to
    the list's head and tail nodes."""

    def __init__(self, node: Optional[ListNode] = None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value: int):
        """Wraps the given value in a ListNode and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly."""

        if self.head:
            self.head.insert_before(value)
            self.head = self.head.prev
        else:
            self.head = ListNode(value)
            self.tail = self.head

        self.length += 1

    def remove_from_head(self):
        """Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node."""

        if self.head is None:
            return None

        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value: int):
        """Wraps the given value in a ListNode and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next pointer accordingly."""

        if self.tail:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        else:
            self.head = ListNode(value)
            self.tail = self.head

        self.length += 1

    def remove_from_tail(self):
        """Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node."""

        if self.tail is None:
            return None

        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node: Optional["ListNode"]):
        """Removes the input node from its current spot in the
        List and inserts it as the new head node of the List."""

        self.delete(node)
        self.add_to_head(node.value)

    def move_to_end(self, node: Optional["ListNode"]):
        """Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List."""

        self.delete(node)
        self.add_to_tail(node.value)

    def delete(self, node: Optional["ListNode"]):
        """Removes a node from the list and handles cases where
        the node was the head or the tail"""

        if not self.head and not self.tail:
            raise Exception

        if node is self.head:
            self.head = self.head.next

        if node is self.tail:
            self.tail = self.tail.prev

        node.delete()
        self.length -= 1

    def get_max(self):
        """Returns the highest value currently in the list"""

        current = self.head
        highest_value = self.head.value

        while current:
            highest_value = current.value if current.value > highest_value else highest_value
            current = current.next

        return highest_value
