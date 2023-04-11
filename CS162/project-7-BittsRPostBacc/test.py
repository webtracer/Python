# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 02/22/2023
# Description: A linkedlist class with recursive functions

class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        """
        Basic costructor for the LinkedList
        :param data:  value to be stored in the node
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A mostly recursive LinkedList class
    """
    def __init__(self):
        """
        Basic Constructor for LinkedList Class
        """
        self._head = None

    def get_head(self):
        """
        getter for head node
        :return:
        """
        return self._head

    def add(self, value):
        """
        function to add objects to the class
        :param value: Value to add to the Linked List
        :return: nothing
        """
        self._head = self.add_helper(self._head, value)

    def add_helper(self, node, value):
        """
        Recursive Helper function for the add function
        :param node: Node to Add to and/or create
        :param value: Value to add to the node
        :return: completed node
        """
        if node is None:
            return Node(value)
        else:
            node.next = self.add_helper(node.next, value)
            return node

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def remove(self, value):
        """
        Removes the specified value from the list
        :param value: value to remove
        :return: Nothing
        """
        self._head = self.remove_helper(self._head, value)

    def remove_helper(self, node_to_check, val_to_remove):
        """
        Recursive helper function for the remove function
        :param node_to_check: Node to check for the value to remove
        :param val_to_remove: value to remove from the linkedlist
        :return: Node with the value removed
        """
        if node_to_check is None:  # If the list is empty
            return 0

        if node_to_check.data == val_to_remove:  # If the node to remove is the head
            node_to_check = node_to_check.next
            return node_to_check

        node_to_check.next = self.remove_helper(node_to_check.next, val_to_remove)
        return node_to_check

    def is_empty(self):
        """
        Function to check if the LinkedList / Node is empty
        :return: None only if the LinkedList is empty
        """
        return self._head is None

    def to_plain_list(self):
        """
        Function to return a list of the data contents of the node
        :return: call to the helper function
        """
        printed_list = []
        return self.to_plain_list_helper(self._head, printed_list)

    def to_plain_list_helper(self, node_to_print, list_to_print):
        """
        Recursive helper function to return a regular list to be printed
        :param node_to_print: Node to print out
        :param list_to_print: Initial blank list to store the output in
        :return: the completed list to print
        """
        if node_to_print is None:
            return []

        list_to_print.append(node_to_print.data)
        self.to_plain_list_helper(node_to_print.next, list_to_print)
        return list_to_print

    def reverse(self):
        """
        Function to reverse the nodes in the LinkedList
        :return:
        """
        self._head = self.reverse_helper(self._head)

    def reverse_helper(self, node_to_reverse):
        """
        Helper function to reverse the contents of the LinkedList
        :param node_to_reverse: the linkedlist to reverse
        :return: reversed node
        """
        if node_to_reverse is None:
            return node_to_reverse

        if node_to_reverse.next is None:
            return node_to_reverse

        reversed_node = self.reverse_helper(node_to_reverse.next)
        node_to_reverse.next.next = node_to_reverse
        node_to_reverse.next = None
        return reversed_node

    def insert(self, value, position):
        """
        Function to insert a value into a specific postion in the LinkedList
        :param value: Value to insert
        :param position: Position in which to insert the value
        :return: nothing
        """
        self._head = self.insert_helper(self._head, value, position)

    def insert_helper(self, node_to_insert_in, item_to_insert, position_to_insert):
        """
        Helper function to insert a value into a specific position in the LinkedList
        :param node_to_insert_in: Node to insert the value in
        :param item_to_insert: Value to insert into the LinkedList
        :param position_to_insert: Position to insert the item into
        :return: updated LinkedList
        """
        if node_to_insert_in is None:
            return node_to_insert_in

        if position_to_insert == 0:
            new_node = Node(item_to_insert)
            new_node.next = node_to_insert_in
            return new_node
        elif position_to_insert == 1:
            new_node = Node(item_to_insert)
            new_node.next = node_to_insert_in.next
            node_to_insert_in.next = new_node
            return node_to_insert_in

        self.insert_helper(node_to_insert_in.next, item_to_insert, position_to_insert-1)
        return node_to_insert_in

    def contains(self, item):
        """
        Function to check if the item exists in the LinkedList
        :param item: Item to look for
        :return: True or false if contained or not
        """
        # self._head = self.contains_helper(self._head,item)
        contained = self.contains_helper(self._head, item)
        return contained

    def contains_helper(self, node_to_check, value):
        """
        Recursive helper function to check if the value exists in the LinkedList
        :param node_to_check: the Node to check for the item
        :param value: Value to check for
        :return: True or False
        """

        if node_to_check is None:
            return False

        if node_to_check.data == value:
            return True
        else:
            return self.contains_helper(node_to_check.next, value)


linked_list_1 = LinkedList()
linked_list_1.add(5)
linked_list_1.add(4)
linked_list_1.add(3)
linked_list_1.add(2)
linked_list_1.add(1)
print(linked_list_1.to_plain_list())
linked_list_1.remove(3)
print(linked_list_1.to_plain_list())
linked_list_1.reverse()
print(linked_list_1.to_plain_list())
linked_list_1.insert(3,2)
print(linked_list_1.to_plain_list())
linked_list_1.reverse()
print(linked_list_1.to_plain_list())
print(linked_list_1.contains(8))
print(linked_list_1.contains(4))
print(linked_list_1.contains(27))
