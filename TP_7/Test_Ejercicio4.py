import unittest
from TP7Ejercicio4 import *


class My_Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bingo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "LOSE")

    def test_2(self):
        self.assertEqual(bingo([20, 12, 23, 14, 6, 22, 12, 17, 2, 26]), "LOSE")

    def test_3(self):
        self.assertEqual(bingo([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]), "WIN")

    def test_4(self):
        self.assertEqual(bingo([5, 2, 13, 7, 5, 14, 17, 15, 9, 10]), "WIN")
