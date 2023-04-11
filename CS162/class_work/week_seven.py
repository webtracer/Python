# Exploration: Linked lists, stacks, queues

class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None


# class LinkedList:
#     """
#     A linked list implementation of the List ADT (abstract data type)
#     """
#     def __init__(self):
#         self._head = None
#
#     def add(self, val):
#         """
#         Adds a node containing val to the end of the linked list
#         """
#         if self._head is None:  # If the list is empty
#             self._head = Node(val)
#         else:
#             current = self._head
#             while current.next is not None:
#                 current = current.next
#             current.next = Node(val)
#
#     def display(self):
#         """
#         Prints out the values in the linked list
#         """
#         current = self._head
#         while current is not None:
#             print(current.data, end=" ")
#             current = current.next
#         print()
#
#     def remove(self, val):
#         """
#         Removes the node containing val from the linked list
#         """
#         if self._head is None:  # If the list is empty
#             return
#
#         if self._head.data == val:  # If the node to remove is the head
#             self._head = self._head.next
#         else:
#             current = self._head
#             while current is not None and current.data != val:
#                 previous = current
#                 current = current.next
#             if current is not None:  # If we found the value in the list
#                 previous.next = current.next
#
#     def is_empty(self):
#         """
#         Returns True if the linked list is empty,
#         returns False otherwise
#         """
#         return self._head is None
#
# # Stacks and queues
#
#
# class Stack:
#     """
#     An implementation of the Stack ADT that uses Python's built-in lists
#     """
#
#     def __init__(self):
#         self.list = []
#
#     def push(self, data):
#         self.list.append(data)
#
#     def pop(self):
#         val = self.list[-1]
#         del self.list[-1]
#         return val
#
#     def peek(self):
#         return self.list[-1]
#
#     def is_empty(self):
#         return len(self.list) == 0
#
#
# class Queue:
#     """
#     An implementation of the Queue ADT that uses Python's built-in lists
#     """
#
#     def __init__(self):
#         self.list = []
#
#     def enqueue(self, data):
#         self.list.append(data)
#
#     def dequeue(self):
#         val = self.list[0]
#         del self.list[0]
#         return val
#
#     def is_empty(self):
#         return len(self.list) == 0


# Quiz Code

# class LinkedList:
#     """
#     A linked list implementation of the List ADT
#     """
#     def __init__(self):
#         self.head = None
#
#     def add(self, val):
#         """
#         Adds a node containing val to the linked list
#         """
#         if self.head is None:  # If the list is empty
#             self.head = Node(val)
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = Node(val)
#
#     def display(self):
#         """
#         Prints out the values in the linked list
#         """
#         current = self.head
#         while current is not None:
#             print(current.data, end=" ")
#             current = current.next
#         print()
#
#     def remove(self, val):
#         """
#         Removes the node containing val from the linked list
#         """
#         if self.head is None:  # If the list is empty
#             return
#
#         if self.head.data == val:  # If the node to remove is the head
#             self.head = self.head.next
#         else:
#             current = self.head
#             while current is not None and current.data != val:
#                 previous = current
#                 current = current.next
#             if current is not None:  # If we found the value in the list
#                 previous.next = current.next
#
#     def is_empty(self):
#         """
#         Returns True if the linked list is empty,
#         returns False otherwise
#         """
#         return self.head is None


class LinkedList:
    """
    A linked list implementation of the List ADT
    """
    def __init__(self):
        self.head = None

    def add(self, val):
        """
        Adds a node containing val to the linked list
        """
        if self.head is None:  # If the list is empty
            self.head = Node(val)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if self.head is None:  # If the list is empty
            return

        if self.head.data == val:  # If the node to remove is the head
            self.head = self.head.next
        else:
            current = self.head
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
        return self.head is None
