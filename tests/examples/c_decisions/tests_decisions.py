import unittest

from src.examples.c_decisions.decisions import is_number_in_range, is_number_not_in_range, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_number_in_a_range(self):
        self.assertEqual(True, is_number_in_range(1, 1, 10))
        self.assertEqual(False, is_number_in_range(0, 1, 10))
        self.assertEqual(True, is_number_in_range(5, 1, 10))

    def test_number_not_in_a_range(self):
        self.assertEqual(True, is_number_not_in_range(0, 1, 10))
        self.assertEqual(True, is_number_not_in_range(11, 1, 10))
        self.assertEqual(False, is_number_not_in_range(5, 1, 10))

