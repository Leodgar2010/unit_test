import unittest
from hw_3_1 import even_odd_number
class TestEvenOddNumber (unittest.TestCase):
    def test_even_odd_even (self):
        self.assertEqual(even_odd_number(2), True)

    def test_even_odd_odd(self):
        self.assertEqual(even_odd_number(3), False)
