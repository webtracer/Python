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
        Returns a regular Python list containing the same values, in the same order, as the linked list
        """
        result = []
        current = self._head
        while current is not None:
            result += [current.data]
            current = current.next
        return result

    def insert(self, value, position):
        """

        :param value:
        :param position:
        :return:
        """

        if self._head is None:
            self.add(value)
            return

        if position == 0:
            temp = self._head
            self._head = Node(value)
            self._head.next = temp
        else:
            current = self._head
            for x in range(position-1):
                if current.next is None:
                    current.next = Node(value)
                    return
                current = current.next
            temp = current.next
            current.next = Node(value)
            current.next.next = temp

        # if position == 0:
        #     self._head.data = value
        #     print(f"self.head data = {self._head.data}")
        #     print(f"previous data = {previous}")
        #     next_val = current.next.data
        #     current.next.data = previous
        #     print(f"after current.data = previous value is: {current.data}")
        #     while current.next is not None:
        #         print(f"in the while next is set {next_val}")
        #         # previous.data = current.data
        #         current.next.data = next_val
        #         print(f"after current.data = next value is {current.next.data}")
        #         current = current.next
        #         if current.next is not None:
        #             next_val = current.next.data
        #         else:
        #             self.add(next_val)
        # else:
        #     while current is not None:
        #         if counter == position:
        #             current.next = current
        #             current.data = value
        #             # while current.next is not None:
        #             # current = current.next
        #             print(current.next)
        #             return
        #         else:
        #             counter += 1
        #             current = current.next


linked_list_1 = LinkedList()
linked_list_1.add(1)
linked_list_1.add(11)
linked_list_1.add(2)
linked_list_1.add(3)
linked_list_1.add(33)
linked_list_1.add(15)
print(linked_list_1.display())
print()
print(linked_list_1.insert(5,0))
print(linked_list_1.display())
# print(linked_list_1.contains(33))
