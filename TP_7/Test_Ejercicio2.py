import unittest
from TP7Ejercicio2 import *


class My_Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(validate_pin("12345"), False)

    def test_2(self):
        self.assertEqual(validate_pin("9765"), True)

    def test_3(self):
        self.assertEqual(validate_pin("a345"), False)

    def test_4(self):
        self.assertEqual(validate_pin("123456"), True)

