import unittest
from week_two import multiply_3_numbers


class TestMultiply3Numbers(unittest.TestCase):
    """

    """

    def test_one(self):
        # multiply_3_numbers(5,2,1)
        self.assertEqual(multiply_3_numbers(5,2,1), 10)

    def test_two(self):
        # multiply_3_numbers(2,2,2)
        self.assertEqual(multiply_3_numbers(2,2,2), 8)

