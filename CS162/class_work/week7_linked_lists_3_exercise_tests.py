import unittest
from LinkedList import LinkedList

class UnitTests(unittest.TestCase):
    def test_test_1(self):
        # Failure message: 
        # This test has no failure messages
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.reverse()
        reg_list = ll.to_regular_list()
        self.assertEqual(reg_list, [3,2,1])
    def test_test_2(self):
        # Failure message: 
        # This test has no failure messages
        ll = LinkedList()
        ll.add(17)
        ll.reverse()
        reg_list = ll.to_regular_list()
        self.assertEqual(reg_list, [17])
