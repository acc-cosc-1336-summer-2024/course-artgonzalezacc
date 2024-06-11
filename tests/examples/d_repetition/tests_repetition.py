import unittest

from src.examples.d_repetition.repetition import sum_of_squares, sum_of_squares_for, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_sum_of_squares_w_value_3(self):
        self.assertEqual(14, sum_of_squares(3))

    def test_sum_of_squares_w_value_4(self):
        self.assertEqual(30, sum_of_squares(4))

    def test_sum_of_squares_w_value_5(self):
        self.assertEqual(55, sum_of_squares(5))

    def test_sum_of_squares_for_w_value_3(self):
        self.assertEqual(14, sum_of_squares_for(3))

