import unittest
from TP7Ejercicio1 import *


class My_Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_of_differences([1, 2, 10]), 9)

    def test_2(self):
        self.assertEqual(sum_of_differences([-3, -2, -1]), 2)

    def test_3(self):
        self.assertEqual(sum_of_differences([-17, 17]), 34)


