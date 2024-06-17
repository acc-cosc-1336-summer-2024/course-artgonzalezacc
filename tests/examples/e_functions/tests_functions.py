import unittest

from src.examples.e_functions.value_return_functions import get_random_int, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_random_int(self):
        random = get_random_int(1, 100)

        self.assertEqual(True, random >= 1)
        self.assertEqual(True, random <= 100)

