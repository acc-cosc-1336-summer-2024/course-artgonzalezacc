import unittest

from src.examples.c_decisions.decisions import get_generation, is_number_in_range, is_number_not_in_range, test_config

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

    def test_get_generation(self):
        
        self.assertEqual('Invalid Option', get_generation(1900))
        self.assertEqual('Centennial', get_generation(2000))
        self.assertEqual('Millenial', get_generation(1990))
        self.assertEqual('Generation X', get_generation(1970))
        self.assertEqual('Baby Boomer', get_generation(1960))
        self.assertEqual('Silent Generation', get_generation(1930))
        self.assertEqual('Invalid Option', get_generation(2025))


