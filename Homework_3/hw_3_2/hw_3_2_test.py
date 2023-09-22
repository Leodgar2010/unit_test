import unittest
from hw_3_2 import number_interval


class TestNumberInterval(unittest.TestCase):
    def test_number_interval_min(self):
        self.assertEqual(number_interval(25), True)

    def test_number_interval_max(self):
        self.assertEqual(number_interval(100), True)

    def test_number_interval_in(self):
        self.assertEqual(number_interval(72), True)

    def test_number_interval_up(self):
        self.assertEqual(number_interval(134), False)

    def test_number_interval_low(self):
        self.assertEqual(number_interval(15), False)
