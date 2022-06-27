import unittest
from TP7Ejercicio3 import *


class My_Test(unittest.TestCase):
    def test_1(self):
        nums = list(range(0, 101))
        nums.remove(5)
        self.assertEqual(missing_no(nums), 5)

    def test_2(self):
        nums = list(reversed(range(0, 101)))
        nums.remove(10)
        self.assertEqual(missing_no(nums), 10)

    def test_3(self):
        nums = list(range(0, 101))
        nums.remove(0)
        self.assertEqual(missing_no(nums), 0)

    def test_4(self):
        nums = list(range(0, 101))
        nums.remove(75)
        self.assertEqual(missing_no(nums), 75)
