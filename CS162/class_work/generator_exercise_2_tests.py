import unittest
from week_eight_generator_exercise_2 import all_primes


class UnitTests(unittest.TestCase):
    def test_all_primes(self):
        primes = all_primes(100)
        prime_list = [next(primes) for i in range(10)]
        self.assertEqual(prime_list, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_testName1(self):
        primes = all_primes(10000)
        for i in range(1000):
            prime_num = next(primes)
        self.assertEqual(prime_num, 7919)


# unittest.main()
