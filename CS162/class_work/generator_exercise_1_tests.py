import unittest
from week_eight_generator_exercise_1 import squares

class UnitTests(unittest.TestCase):
    def test_testName(self):
        self.assertEqual([n for n in squares], [x * x for x in range(1, 101)])
