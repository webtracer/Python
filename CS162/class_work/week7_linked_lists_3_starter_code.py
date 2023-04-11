class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A linked list implementation of the List ADT
    """
    def __init__(self):
        self._head = None

    def add(self, val):
        """
        Adds a node containing val to the linked list
        """
        if self._head is None:  # If the list is empty
            self._head = Node(val)
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if self._head is None:  # If the list is empty
            return

        if self._head.data == val:  # If the node to remove is the head
            self._head = self._head.next
        else:
            current = self._head
            while current is not None and current.data != val:
                previous = current
                current = current.next
            if current is not None:  # If we found the value in the list
                previous.next = current.next

    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self._head is None

    def to_regular_list(self):
        """
        Returns a regular Python list containing the same values,
        in the same order, as the linked list
        """
        result = []
        current = self._head
        while current is not None:
            result += [current.data]
            current = current.next
        return result

    def reverse(self):
        """

        :return:
        """
        previous = None
        current = self._head

        while current is not None:
            next_item = current.next
            current.next = previous
            previous = current
            current = next_item
        self._head = previous


linked_list_1 = LinkedList()
linked_list_1.add(1)
linked_list_1.add(11)
linked_list_1.add(2)
linked_list_1.add(3)
linked_list_1.add(33)
linked_list_1.add(15)
print(linked_list_1.display())
linked_list_1.reverse()
print(linked_list_1.display())
